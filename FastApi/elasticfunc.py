from elasticsearch import Elasticsearch
from datetime import datetime
import requests
from pprint import pprint
import json
#On local connect pc
es = Elasticsearch(hosts="http://46.48.3.74:9200")
#On server connect
#es = Elasticsearch(hosts="http://localhost:9200")


def old_get_data_id(doc_id: str) -> dict:
    resp = es.search(index=['private_face','legal_face'], query={'bool':{'must':{'match':{'_id':doc_id}}}})
    return check_response(resp)

def get_data_id(doc_id: str) -> dict:
    resp = es.search(index=['private_face','legal_face'], query={'bool':{'must':{'match':{'_id':doc_id}}}})
    return resp

def get_data_text(full_text: str):
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


def check_response(resp):
    if resp['hits']['total']['value'] != 0:
        return resp["hits"]["hits"][0]["_source"]
    else:
        return {'message': 'Not Found'}


def find_id_doc(full_text: str, indexes = ['private_face','legal_face']):
    tokens = es.indices.analyze(analyzer="standard", field='text', text=full_text)['tokens']
    resp = get_response(indexes, tokens)
    if resp['hits']['total']['value'] != 0:
        return resp["hits"]["hits"][0]["_id"]
    else:
        return 'Not Found'

def find_doc_filter(full_text: str, regions:list=[], okveds:list = [], indexes = ['private_face','legal_face']):
    tokens = es.indices.analyze(analyzer="standard", field='text', text=full_text)['tokens']
    query = [{"multi_match":
                  {'query': token['token'],
                   'fields': "*"}}
             for token in tokens]
    resp = es.search(index=indexes, query={
        "bool": {
            "should": [{
                "multi_match":{
                    "query": full_text,
                    'fields': ["inn", 'name', 'first_name','last_name', 'patronymic'],
                    "auto_generate_synonyms_phrase_query": True,
                    "fuzziness": 2,
                    #"minimum_should_match": "70%",
                    "operator": "or"
                }
            }],
            "minimum_should_match": 1,
            "filter":[
                {"terms":{"region":regions}},
                {"terms":{"okved":okveds}}
            ]
        }
    })
    pprint(resp)
    if resp['hits']['total']['value'] != 0:
        return resp["hits"]["hits"][0]["_source"]
    else:
        return {'message':'Not Found'}


def get_response(indexes, tokens):
    query = [{"multi_match":
                  {'query': token['token'],
                   'fields': "*"}}
             for token in tokens]
    if 'legal_face' in indexes:
        pass
            #query.append({'match': {'region' : region}})
    pprint(query)
    resp = es.search(index=indexes, query={
        "bool": {
            "must": query
        }
    })
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

def create_edge(item: dict) -> list:
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


# test
# print(get_data_id(6434))
# print(get_data_all_info(inn="7712345678904", lastname="Шульц"))
# print(get_data_all_info(inn="7712345678900"))
# print(get_data_text("Владew Тарасович"))
# test_data_from_db = [{"child": "73", "parent": "16", "kind": "1", "depth": 0}, {"child": "73", "parent": "95", "kind": "1", "depth": 0}, {"child": "73", "parent": "300", "kind": "1", "depth": 0}, {"child": "73", "parent": "38", "kind": "1", "depth": 0}, {"child": "73", "parent": "64", "kind": "1", "depth": 0}, {"child": "73", "parent": "282", "kind": "1", "depth": 0}, {"child": "73", "parent": "133", "kind": "2", "depth": 0}, {"child": "179", "parent": "84", "kind": "1", "depth": 1}, {"child": "179", "parent": "162", "kind": "1", "depth": 1}, {"child": "179", "parent": "223", "kind": "1", "depth": 1}, {"child": "179", "parent": "16", "kind": "1", "depth": 1}, {"child": "179", "parent": "46", "kind": "1", "depth": 1}, {"child": "179", "parent": "238", "kind": "1", "depth": 1}, {"child": "179", "parent": "238", "kind": "1", "depth": 1}, {"child": "179", "parent": "123", "kind": "1", "depth": 1}, {"child": "179", "parent": "74", "kind": "1", "depth": 1}, {"child": "179", "parent": "31", "kind": "1", "depth": 1}, {"child": "179", "parent": "257", "kind": "2", "depth": 1}, {"child": "124", "parent": "70", "kind": "1", "depth": 1}, {"child": "124", "parent": "210", "kind": "1", "depth": 1}, {"child": "124", "parent": "95", "kind": "1", "depth": 1}, {"child": "124", "parent": "220", "kind": "1", "depth": 1}, {"child": "124", "parent": "196", "kind": "1", "depth": 1}, {"child": "124", "parent": "141", "kind": "2", "depth": 1}, {"child": "220", "parent": "246", "kind": "1", "depth": 1}, {"child": "220", "parent": "217", "kind": "1", "depth": 1}, {"child": "220", "parent": "3", "kind": "1", "depth": 1}, {"child": "220", "parent": "20", "kind": "1", "depth": 1}, {"child": "220", "parent": "2", "kind": "1", "depth": 1}, {"child": "220", "parent": "16", "kind": "2", "depth": 1}, {"child": "147", "parent": "224", "kind": "1", "depth": 1}, {"child": "147", "parent": "128", "kind": "1", "depth": 1}, {"child": "147", "parent": "282", "kind": "1", "depth": 1}, {"child": "147", "parent": "10", "kind": "1", "depth": 1}, {"child": "147", "parent": "296", "kind": "1", "depth": 1}, {"child": "147", "parent": "37", "kind": "1", "depth": 1}, {"child": "147", "parent": "82", "kind": "1", "depth": 1}, {"child": "147", "parent": "30", "kind": "1", "depth": 1}, {"child": "147", "parent": "257", "kind": "1", "depth": 1}, {"child": "147", "parent": "12", "kind": "1", "depth": 1}, {"child": "147", "parent": "174", "kind": "1", "depth": 1}, {"child": "147", "parent": "1", "kind": "2", "depth": 1}, {"child": "298", "parent": "193", "kind": "1", "depth": 1}, {"child": "298", "parent": "133", "kind": "1", "depth": 1}, {"child": "298", "parent": "279", "kind": "1", "depth": 1}, {"child": "298", "parent": "139", "kind": "1", "depth": 1}, {"child": "298", "parent": "214", "kind": "1", "depth": 1}, {"child": "298", "parent": "196", "kind": "1", "depth": 1}, {"child": "298", "parent": "74", "kind": "1", "depth": 1}, {"child": "298", "parent": "7", "kind": "2", "depth": 1}, {"child": "76", "parent": "246", "kind": "1", "depth": 2}, {"child": "76", "parent": "74", "kind": "1", "depth": 2}, {"child": "76", "parent": "294", "kind": "1", "depth": 2}, {"child": "76", "parent": "128", "kind": "1", "depth": 2}, {"child": "76", "parent": "196", "kind": "2", "depth": 2}]

#print(filling_data([{'child' : 1, 'parent' : 2, 'kind' : 1, 'depth' : 1}, {'child' : 2, 'parent' : 3, 'kind' : 1, 'depth' : 2}]))
#pprint(filling_data(test_data_from_db))
#print("\n\n")
#print("--------------------------------------------------------------------------")
#print("\n\n")
#pprint(filling_data_v2(test_data_from_db)
#pprint(find_id_doc("Влад Тарасович"))
