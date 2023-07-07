from elasticsearch import Elasticsearch
from datetime import datetime
import requests

es = Elasticsearch(hosts="http://46.48.3.74:9200")


def get_data_id(doc_id: str):
    resp = es.get(index='private_face', id=doc_id)
    return resp["_source"]


def get_data_text(full_text: str):
    tokens = es.indices.analyze(index='private_face', analyzer="standard", field='text', text=full_text)['tokens']
    query = [{"multi_match":
                  {'query': token['token'],
                   'fields': "*"}}
             for token in tokens]
    resp = es.search(index='private_face', query={
        "bool": {
            "should": query
        }
    })
    return [resp["hits"]["hits"][0]["_source"]]


# delete?
def get_data_test_inn(inn: str):
    resp = es.search(index='private_face', query={
        "match": {
            "inn": inn
        }
    })
    return resp["hits"]["hits"][0]["_source"]


# delete?
def get_data_all_info(inn="", firstname="", lastname="", patronimyc="", name=""):
    resp = es.search(index='private_face', query={
        "bool": {
            "should": [
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
                    "match": {"patronymic": patronimyc}
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
# print(get_data_all_info(inn="7712345678900"))
# print(get_data_text("Влад Тарасович"))
