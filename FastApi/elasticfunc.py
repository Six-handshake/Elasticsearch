from elasticsearch import Elasticsearch
from datetime import datetime
import requests
from pprint import pprint
import json
#On local connect pc
es = Elasticsearch(hosts="http://46.48.3.74:9200")
#On server connect
#es = Elasticsearch(hosts="http://localhost:9200")

default_indexes = ['private_face', 'legal_face']

def old_get_data_id(doc_id:str) -> dict:
    resp = es.search(index=['private_face','legal_face'], query={'bool':{'must':{'match':{'_id':doc_id}}}})
    return check_response(resp)

def get_data_id(doc_id:str) -> dict:
    resp = es.search(index=['private_face','legal_face'], query={'bool':{'must':{'match':{'_id':doc_id}}}})
    return resp

def get_indexes(is_person:bool, is_company:bool) -> list:
    indexes = []
    if is_person:
        indexes.append(default_indexes[0])
    if is_company:
        indexes.append(default_indexes[1])
    return indexes

def get_data_text(full_text:str) -> dict:
    print(full_text)
    tokens = es.indices.analyze(analyzer="standard", field='text', text=full_text)['tokens']
    query = [{"multi_match":
                  {'query': token['token'],
                   'fields': "*"}}
             for token in tokens]
    resp = es.search(index=['private_face','legal_face'], query={
        "bool": {
            "must": query
        }
    })
    return check_response(resp)


def check_response(resp:dict) -> dict:
    if resp['hits']['total']['value'] != 0:
        return resp["hits"]["hits"][0]["_source"]
    else:
        return {'message': 'Not Found'}


def find_id_doc(full_text:str, indexes:list = default_indexes) -> str:
    tokens = es.indices.analyze(analyzer="standard", field='text', text=full_text)['tokens']
    resp = get_response(indexes, tokens)
    if resp['hits']['total']['value'] != 0:
        return resp["hits"]["hits"][0]["_id"]
    else:
        return 'Not Found'

def find_doc_filter(full_text:str, regions:list=[], okveds:list = [], indexes:list = default_indexes) -> list:
    #как объединить???
    tokens = es.indices.analyze(analyzer="standard", field='text', text=full_text)['tokens']
    resp = es.search(index=indexes, size=10, query=get_filter_query(tokens, okveds, regions))
    pprint(resp)
    if resp['hits']['total']['value'] != 0:
        return get_variants_dict(resp["hits"]["hits"])
    else:
        return []

def get_variants_dict(data:list) -> list:
    result = []
    for item in data:
        obj = {}
        source = item['_source']
        pprint(item['_source'])
        if item['_index'] == 'legal_face':
            obj['text'] = source['name']
            obj['is_person'] = False
            obj['is_company'] = True
        elif item['_index'] == 'private_face':
            obj['text'] = ' '.join([source['firstname'], source['lastname'], source['patronymyic']])
            obj['is_person'] = False
            obj['is_company'] = True
        obj['inn'] = source['inn']
        obj['okved'] = source['okved']
        obj['region'] = source['region']
        result.append(obj)
    return result


def get_filter_query(tokens:list, okveds:list = [], regions:list = []) -> dict:
    pprint(tokens)
    query = [{"multi_match": {'query': token['token'],
                              'type': 'phrase_prefix',
                              'fields': ["inn^5", 'name^4', 'first_name^3', 'last_name^4', 'patronymic']}}
              for token in tokens]
    text = ' '.join([item['token'] for item in tokens])
    tokens = es.indices.analyze(analyzer="russian", field='text', text=text)['tokens']
    pprint(tokens)
    query += [{"multi_match": {'query': token['token'],
                              'type': 'phrase_prefix',
                              'fields': ["inn", 'name', 'first_name', 'last_name', 'patronymic']}
               }
             for token in tokens]
    minimum_match = str(len(tokens))+"<80%"
    main_query = {
        "bool": {
            "should": query,
            "minimum_should_match": minimum_match,
        }
    }
    if len(okveds) > 0 or len(regions) > 0:
        main_query["bool"]["filter"] = []
        if len(okveds) > 0:
            main_query["bool"]["filter"].append({"terms": {"okved": okveds}})
        if len(regions) > 0:
            main_query["bool"]["filter"].append({"terms": {"region": regions}})
    return main_query


def get_response(indexes:list, tokens:list) -> dict:
    query = [{"multi_match":{'query': token['token'],'fields': "*"}}
             for token in tokens]
    if 'legal_face' in indexes:
        pass
            #query.append({'match': {'region' : region}})
    pprint(query)
    resp = es.search(index=indexes, query={"bool": {"must": query}})
    return resp


def filling_data(data:list) -> list:
    res = []
    for item in data:
        doc = dict()
        doc['parent'] = old_get_data_id(str(item['parent']))
        doc['parent']['kind'] = item['kind']
        doc['child'] = old_get_data_id(str(item['child']))
        doc['child']['kind'] = item['kind']
        doc['depth'] = item['depth']
        res.append(doc)
    return res

def create_node(obj_id:str, depth_x:str, depth_y:str,child_id:str = "") -> dict:
    res = dict()
    resp = get_data_id(obj_id)
    res['id'] = child_id+'_'+obj_id if child_id != "" else obj_id
    res['info'] = check_response(resp)
    res['type'] = resp['hits']['hits'][0]['_index']
    res['depth_x'] = depth_x
    res['depth_y'] = depth_y
    res['is_child'] = True if child_id == "" else False
    return res

def create_edge(item:dict) -> list:
    edges = [{'parent_id': item['child'] + "_" + item['parent'],
              'child_id': item['child'],
              'kind': item['kind'],
              'share': item['share'],
              'date_begin': item['date_begin'],
              'date_end': item['date_end']}]
    for link in item["links"]:
        edges.append({'parent_id': link['child_id'] + "_" + item['parent'],
                      'child_id': item['child'],
                      'kind': item['kind'],
                      'share': item['share'],
                      'date_begin': item['date_begin'],
                      'date_end': item['date_end']})
    return edges

def filling_data_v2(data:list) -> list:
    nodes = []
    edge = []
    last_child = -1
    last_depth = -1
    depth_y = 0
    for item in data:
        if last_depth != item['depth']:
            depth_y = 0
            last_depth = item['depth']
        if item['child'] != last_child:
            nodes.append(create_node(obj_id = item['child'],
                                     depth_x = item['depth'],
                                     depth_y = depth_y))
            depth_y+=1
            last_child = item['child']
        nodes.append(create_node(obj_id = item['parent'],
                                 depth_x = item['depth'],
                                 depth_y = depth_y,
                                 child_id = item['child']))
        depth_y+=1
        edge += create_edge(item)
    return nodes, edge