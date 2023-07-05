from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(hosts="http://46.48.3.74:9200")


def get_data_id(doc_id: str):
    resp = es.get(index='private_face', id=doc_id)
    return resp["_source"]


def get_data_text(full_text: str):
    # TODO:analizator,tokenizator and search in elasticsearch
    return "Later..."


def get_data_test_inn(inn: str):
    resp = es.search(index='private_face', query={
        "match": {
            "inn": inn
        }
    })
    return resp["hits"]["hits"][0]["_source"]


def get_data_all_info(inn="", fn="", sn="", p="", name=""):
    resp = es.search(index='private_face', query={
        "bool": {
            "should": [
                {
                    "match": {"inn": inn}
                },
                {
                    "match": {"firstname": fn}
                },
                {
                    "match": {"secondname": sn}
                },
                {
                    "match": {"patronymic": p}
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
print(GetDataAllInfo(inn="7712345678904", name="Best company"))
print(GetDataAllInfo(inn="7712345678900"))
