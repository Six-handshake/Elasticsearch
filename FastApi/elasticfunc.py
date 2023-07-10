from elasticsearch import Elasticsearch
from datetime import datetime
import requests

es = Elasticsearch(hosts="http://localhost:9200")


def get_data_id(doc_id: str):
    resp = es.get(index='private_face', id=doc_id)
    return resp["_source"]


def get_data_text(full_text: str):
    print(full_text)
    tokens = es.indices.analyze(index='private_face', analyzer="standard", field='text', text=full_text)['tokens']
    query = [{"multi_match":
                  {'query': token['token'],
                   'fields': "*"}}
             for token in tokens]
    resp = es.search(index='private_face', query={
        "bool": {
            "must": query
        }
    })
    if resp['hits']['total']['value']!=0:
        return resp["hits"]["hits"][0]["_source"]
    else:
        return [{'message': 'Not Found'}]


# delete?
def get_data_test_inn(inn: str):
    resp = es.search(index='private_face', query={
        "match": {
            "inn": inn
        }
    })
    return resp["hits"]["hits"][0]["_source"]


# delete?
def get_data_all_info(inn="", firstname="", lastname="", patronymic="", name=""):
    resp = es.search(index='private_face', query={
        "bool": {
            "Should": [
                {
                    "match": {"inn": inn}
                },
                {
                    "match": {"firstname": firstname}
                },
                {
                    "match": {"lastname": lastname}
                },
                {
                    "match": {"patronymic": patronymic}
                },
                {
                    "match": {"name": name}
                }
            ]
        }
    })
    return resp

# test
# print(GetDataId(1))
# print(GetDataText("Иванов"))
# print(GetDataTestInn("7712345678900"))
# print(get_data_all_info(inn="7712345678904", lastname="Шульц"))
#print(get_data_all_info(inn="7712345678900"))
print(get_data_text("Владew Тарасович"))
