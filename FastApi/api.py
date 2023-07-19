from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
from typing import Union
import json
import elasticfunc
from pprint import pprint
sys.path.append('/home/serv/postgre/Postgres/src')
sys.path.append('/home/serv/elasticsearch/Elasticsearch')
#import json_loader
app = FastAPI()

# React connects
origins = [
    "http://localhost:8000",
    "localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

test = []

todos = [
    {
        "id": "1",
        "message": "Read a book."
    },
    {
        "id": "2",
        "message": "Cycle around town."
    }
]

@app.post("/api/p_test",tags=["p_test"])
async def p_test():
    return json_loader.generate_json("72","54")


@app.get("/api", tags=["root"])
async def read_root() -> dict:
    return {"data": [{"message": " Hello World"}]}


@app.get("/api/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.post("/api/todo", tags=["todos"])
async def add_test_data(test_data: dict) -> dict:
    todos.append(test_data)
    return {
        "data": {"Test data added."}
    }

test_data_from_db = [{'child': '73',
  'date_begin': '2018-05-31',
  'date_end': 'None',
  'depth': 0,
  'kind': '2',
  'links': [],
  'parent': '188',
  'share': 'None'},
 {'child': '73',
  'date_begin': '2022-02-27',
  'date_end': '2016-01-20',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '178',
  'share': '44.05'},
 {'child': '73',
  'date_begin': '2021-11-08',
  'date_end': '2016-03-08',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '569',
  'share': '27.15'},
 {'child': '73',
  'date_begin': '2021-11-05',
  'date_end': '2016-02-19',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '233',
  'share': '12.21'},
 {'child': '73',
  'date_begin': '2019-05-05',
  'date_end': 'None',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '823',
  'share': '10.03'},
 {'child': '73',
  'date_begin': '2021-01-16',
  'date_end': 'None',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '54',
  'share': '4.14'},
 {'child': '73',
  'date_begin': '2021-10-27',
  'date_end': 'None',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '227',
  'share': '1.4'},
 {'child': '73',
  'date_begin': '2019-11-25',
  'date_end': 'None',
  'depth': 0,
  'kind': '1',
  'links': [],
  'parent': '629',
  'share': '1.02'},
 {'child': '718',
  'date_begin': '2017-07-22',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '602',
  'share': 'None'},
 {'child': '601',
  'date_begin': '2012-12-24',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '815',
  'share': 'None'},
 {'child': '219',
  'date_begin': '2013-03-23',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '151',
  'share': 'None'},
 {'child': '476',
  'date_begin': '2013-05-04',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '684',
  'share': 'None'},
 {'child': '1014',
  'date_begin': '2019-06-23',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '962',
  'share': 'None'},
 {'child': '433',
  'date_begin': '2018-05-07',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '985',
  'share': 'None'},
 {'child': '991',
  'date_begin': '2012-06-26',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '453',
  'share': 'None'},
 {'child': '441',
  'date_begin': '2014-10-08',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '630',
  'share': 'None'},
 {'child': '713',
  'date_begin': '2013-03-06',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '435',
  'share': 'None'},
 {'child': '960',
  'date_begin': '2018-06-28',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [{'child_id': '73', 'object_id': 5, 'type': 'parent'}],
  'parent': '54',
  'share': 'None'},
 {'child': '570',
  'date_begin': '2011-01-03',
  'date_end': 'None',
  'depth': 1,
  'kind': '2',
  'links': [],
  'parent': '156',
  'share': 'None'},
 {'child': '219',
  'date_begin': '2016-04-03',
  'date_end': '2014-10-12',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '459',
  'share': '4.02'},
 {'child': '1014',
  'date_begin': '2023-05-10',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 5, 'type': 'parent'}],
  'parent': '54',
  'share': '4.01'},
 {'child': '570',
  'date_begin': '2017-08-13',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '568',
  'share': '3.03'},
 {'child': '219',
  'date_begin': '2018-08-24',
  'date_end': '2015-05-20',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 6, 'type': 'parent'}],
  'parent': '227',
  'share': '3.01'},
 {'child': '601',
  'date_begin': '2018-02-06',
  'date_end': '2014-10-08',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '459',
  'share': '2.01'},
 {'child': '476',
  'date_begin': '2013-11-18',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 6, 'type': 'parent'}],
  'parent': '227',
  'share': '2.01'},
 {'child': '601',
  'date_begin': '2017-06-12',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '495',
  'share': '2.01'},
 {'child': '441',
  'date_begin': '2022-04-07',
  'date_end': '2014-09-26',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '524',
  'share': '1.04'},
 {'child': '441',
  'date_begin': '2015-03-13',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 6, 'type': 'parent'}],
  'parent': '227',
  'share': '1.02'},
 {'child': '713',
  'date_begin': '2020-08-06',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '459',
  'share': '1.02'},
 {'child': '601',
  'date_begin': '2014-12-25',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 4, 'type': 'parent'}],
  'parent': '823',
  'share': '1.02'},
 {'child': '1014',
  'date_begin': '2021-05-17',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '568',
  'share': '1.01'},
 {'child': '476',
  'date_begin': '2016-12-31',
  'date_end': '2015-07-11',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '222',
  'share': '1.01'},
 {'child': '960',
  'date_begin': '2019-05-09',
  'date_end': '2014-10-06',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 1, 'type': 'parent'}],
  'parent': '178',
  'share': '1.01'},
 {'child': '713',
  'date_begin': '2016-01-25',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 6, 'type': 'parent'}],
  'parent': '227',
  'share': '1.01'},
 {'child': '991',
  'date_begin': '2019-03-12',
  'date_end': '2015-09-21',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 6, 'type': 'parent'}],
  'parent': '227',
  'share': '1.01'},
 {'child': '960',
  'date_begin': '2021-12-30',
  'date_end': '2015-06-12',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '495',
  'share': '1.01'},
 {'child': '433',
  'date_begin': '2023-02-12',
  'date_end': '2016-01-18',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '459',
  'share': '1.01'},
 {'child': '433',
  'date_begin': '2020-04-15',
  'date_end': '2015-12-31',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 3, 'type': 'parent'}],
  'parent': '233',
  'share': '1.01'},
 {'child': '991',
  'date_begin': '2013-02-15',
  'date_end': '2015-02-22',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '568',
  'share': '1.01'},
 {'child': '718',
  'date_begin': '2021-02-17',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [],
  'parent': '568',
  'share': '1.01'},
 {'child': '570',
  'date_begin': '2016-10-20',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 3, 'type': 'parent'}],
  'parent': '233',
  'share': '1.01'},
 {'child': '718',
  'date_begin': '2022-02-14',
  'date_end': 'None',
  'depth': 1,
  'kind': '1',
  'links': [{'child_id': '73', 'object_id': 3, 'type': 'parent'}],
  'parent': '233',
  'share': '1.01'},
 {'child': '16',
  'date_begin': '2017-06-15',
  'date_end': 'None',
  'depth': 2,
  'kind': '2',
  'links': [{'child_id': '601', 'object_id': 25, 'type': 'parent'},
            {'child_id': '960', 'object_id': 35, 'type': 'parent'}],
  'parent': '495',
  'share': 'None'},
 {'child': '16',
  'date_begin': '2022-01-23',
  'date_end': '2015-09-16',
  'depth': 2,
  'kind': '1',
  'links': [{'child_id': '570', 'object_id': 21, 'type': 'parent'},
            {'child_id': '1014', 'object_id': 30, 'type': 'parent'},
            {'child_id': '991', 'object_id': 38, 'type': 'parent'},
            {'child_id': '718', 'object_id': 39, 'type': 'parent'}],
  'parent': '568',
  'share': '49.33'},
 {'child': '16',
  'date_begin': '2022-07-08',
  'date_end': 'None',
  'depth': 2,
  'kind': '1',
  'links': [{'child_id': '441', 'object_id': 26, 'type': 'parent'}],
  'parent': '524',
  'share': '37.42'},
 {'child': '16',
  'date_begin': '2020-04-05',
  'date_end': '2015-12-16',
  'depth': 2,
  'kind': '1',
  'links': [{'child_id': '219', 'object_id': 19, 'type': 'parent'},
            {'child_id': '601', 'object_id': 23, 'type': 'parent'},
            {'child_id': '713', 'object_id': 28, 'type': 'parent'},
            {'child_id': '433', 'object_id': 36, 'type': 'parent'}],
  'parent': '459',
  'share': '11.23'},
 {'child': '16',
  'date_begin': '2022-07-05',
  'date_end': 'None',
  'depth': 2,
  'kind': '1',
  'links': [{'child_id': '476', 'object_id': 31, 'type': 'parent'}],
  'parent': '222',
  'share': '2.02'}]

@app.get('/api/front_v1',tags=['front-test'])
async def test_front_v1() -> list:
    return elasticfunc.filling_data(test_data_from_db)

@app.get('/api/front_v2',tags=['front-test'])
async def test_front_v2() -> dict:
    nodes, edges = elasticfunc.filling_data_v2(test_data_from_db)
    return {"nodes": nodes,
            "edges": edges}

@app.get("/api/id/{doc_id}", tags=["main"])
async def get_doc_for_id(doc_id: str, q: Union[str, None] = None) -> dict:
    print("start")
    return elasticfunc.get_data_id(doc_id)

@app.post("/api/find_path", tags=["main"])
async def get_test_filter(data:dict) -> list:
    text = data['text']
    regions = data['regions'] if 'regions' in data else []
    okved = data['okved'] if 'okved' in data else []
    return elasticfunc.find_doc_filter(text, regions, okved)


@app.post("/api/find", tags=["main"])
async def get_doc_for_text(data: dict) -> dict:
    index1_indexes = elasticfunc.get_indexes(data['index1']['is_person'], data['index1']['is_company'])
    if len(index1_indexes) <= 0:
        return {"message":"Error: Don't select type obj found"}
    index1_id = elasticfunc.find_id_doc(data['index1']['data'], index1_indexes)
    index2_id = None
    if 'index2' in data:
        if data['index2'] != "":
            index2_indexes = elasticfunc.get_indexes(data['index2']['is_person'], data['index2']['is_company'])
            if len(index2_indexes) <= 0:
                return {"message": "Error: Don't select type obj found"}
            index2_id = elasticfunc.find_id_doc(data['index2']['data'], index2_indexes)
    if index2_id is not None:
        data = json_loader.generate_json(index1_id, index2_id)
    else:
        pass
    if data != "null":
        nodes, edges = elasticfunc.filling_data_v2(data)
        return {'nodes': nodes,
                'edges':edges}
    else:
        return {"message": "Not found agent's links"}