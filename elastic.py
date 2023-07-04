from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://46.48.3.74:9200")

print(es.info())
