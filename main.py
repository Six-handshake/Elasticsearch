from datetime import datetime
from elasticsearch import Elasticsearch
# create a connection to Elasticsearch
ELASTIC_PASSWORD = "sPPhehZErZpDMuQMe8ES"
path = "D:/Downloads/elasticsearch-8.8.2-windows-x86_64/elasticsearch-8.8.2/config/certs/http_ca.crt"
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs=path,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Successful response!
print(client.info())