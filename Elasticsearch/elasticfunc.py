from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(hosts="http://46.48.3.74:9200")

def GetDataId(doc_id : str):
    resp = es.get(index='private_face',id=doc_id)
    return resp["_source"]

def GetDataText(full_text : str):
    #TODO:analizator,tokenizator and search in elasticsearch
    return "Later..."

def GetDataTestInn(inn : str):
    resp = es.search(index='private_face', query= {
        "match": {
            "inn": inn
        }
    })
    return resp["hits"]["hits"][0]["_source"]

#test
#print(GetDataId(1))
#print(GetDataText("Иванов"))
#print(GetDataTestInn("7712345678900"))