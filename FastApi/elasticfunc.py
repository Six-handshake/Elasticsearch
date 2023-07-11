from elasticsearch import Elasticsearch
from datetime import datetime
import requests
from pprint import pprint
#On local connect pc
#es = Elasticsearch(hosts="http://46.48.3.74:9200")
#On server connect
es = Elasticsearch(hosts="http://localhost:9200")


def get_data_id(doc_id: str) -> dict:
    resp = es.search(index=['private_face','legal_face'], query={'bool':{'must':{'match':{'_id':doc_id}}}})
    return check_response(resp)


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
        resp['hits']['hits'][0]['_source']['id'] = resp["hits"]["hits"][0]["_id"]
        return resp["hits"]["hits"][0]["_source"]
    else:
        return {'message': 'Not Found'}


def find_id_doc(full_text: str):
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
    if resp['hits']['total']['value'] != 0:
        return resp["hits"]["hits"][0]["_id"]
    else:
        return 'Not Found'

def filling_data(data:list) -> list:
    res = []
    for item in data:
        doc = dict()
        doc['parent'] = get_data_id(str(item['parent']))
        doc['child'] = get_data_id(str(item['child']))
        doc['depth'] = item['depth']
        res.append(doc)
    return res

def filling_data_v2(data:list) -> list:
    res = []
    last_child = -1
    doc = dict()
    for item in data:
        if item['child'] != last_child:
            last_child = item['child']
            if len(doc)>0:
                res.append(doc)
            doc = dict()
            doc['child'] = get_data_id(str(item['child']))
            doc['depth'] = item['depth']
            doc['parents'] = list()

        doc['parents'].append(get_data_id(str(item['parent'])))
    if len(doc) > 0:
        res.append(doc)
    return res

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
#pprint(filling_data_v2(test_data_from_db))
<<<<<<< HEAD
pprint(find_id_doc("Влад Тарасович"))
=======
#pprint(find_id_doc("Влад Тарасович"))
>>>>>>> be338a5e76ca76f2f9531eebf79a0f1eb7d9a98c
