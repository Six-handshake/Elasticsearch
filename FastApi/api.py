from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
from typing import Union
import json
import elasticfunc
from pprint import pprint
sys.path.append('/home/serv/elasticsearch/Elasticsearch/Postgres/src')
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

test_data_from_db = [{"child": "73", "parent": "188", "kind": "2", "date_begin": "2018-05-31", "date_end": "None", "share": "None", "depth": 0, "links": []}, {"child": "73", "parent": "178", "kind": "1", "date_begin": "2022-02-27", "date_end": "2016-01-20", "share": "44.05", "depth": 0, "links": []}, {"child": "73", "parent": "569", "kind": "1", "date_begin": "2021-11-08", "date_end": "2016-03-08", "share": "27.15", "depth": 0, "links": []}, {"child": "73", "parent": "233", "kind": "1", "date_begin": "2021-11-05", "date_end": "2016-02-19", "share": "12.21", "depth": 0, "links": []}, {"child": "73", "parent": "823", "kind": "1", "date_begin": "2019-05-05", "date_end": "None", "share": "10.03", "depth": 0, "links": []}, {"child": "73", "parent": "54", "kind": "1", "date_begin": "2021-01-16", "date_end": "None", "share": "4.14", "depth": 0, "links": []}, {"child": "73", "parent": "227", "kind": "1", "date_begin": "2021-10-27", "date_end": "None", "share": "1.4", "depth": 0, "links": []}, {"child": "73", "parent": "629", "kind": "1", "date_begin": "2019-11-25", "date_end": "None", "share": "1.02", "depth": 0, "links": []}, {"child": "433", "parent": "985", "kind": "2", "date_begin": "2018-05-07", "date_end": "None", "share": "None", "depth": 1, "links": []}, {"child": "433", "parent": "856", "kind": "1", "date_begin": "2019-02-18", "date_end": "2015-02-13", "share": "3.02", "depth": 1, "links": []}, {"child": "433", "parent": "626", "kind": "1", "date_begin": "2018-05-15", "date_end": "2014-11-16", "share": "2.02", "depth": 1, "links": []}, {"child": "433", "parent": "418", "kind": "1", "date_begin": "2021-09-19", "date_end": "None", "share": "2.02", "depth": 1, "links": []}, {"child": "433", "parent": "640", "kind": "1", "date_begin": "2019-07-01", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "195", "kind": "1", "date_begin": "2019-10-14", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "324", "kind": "1", "date_begin": "2021-02-13", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "76", "kind": "1", "date_begin": "2020-09-12", "date_end": "2014-10-21", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "532", "kind": "1", "date_begin": "2023-03-16", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "324", "kind": "1", "date_begin": "2022-03-26", "date_end": "2015-06-05", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "400", "kind": "1", "date_begin": "2022-05-30", "date_end": "2015-01-16", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "87", "kind": "1", "date_begin": "2019-08-18", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "955", "kind": "1", "date_begin": "2023-04-23", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "965", "kind": "1", "date_begin": "2023-03-21", "date_end": "None", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "225", "kind": "1", "date_begin": "2020-03-19", "date_end": "2014-12-04", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "870", "kind": "1", "date_begin": "2019-07-24", "date_end": "2015-07-01", "share": "2.01", "depth": 1, "links": []}, {"child": "433", "parent": "358", "kind": "1", "date_begin": "2020-12-23", "date_end": "None", "share": "1.05", "depth": 1, "links": []}, {"child": "433", "parent": "310", "kind": "1", "date_begin": "2019-09-12", "date_end": "2015-02-17", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "488", "kind": "1", "date_begin": "2018-08-21", "date_end": "2015-12-23", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "587", "kind": "1", "date_begin": "2021-12-30", "date_end": "2015-12-20", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "132", "kind": "1", "date_begin": "2020-04-29", "date_end": "None", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "339", "kind": "1", "date_begin": "2019-04-16", "date_end": "None", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "547", "kind": "1", "date_begin": "2019-04-11", "date_end": "2015-10-14", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "479", "kind": "1", "date_begin": "2023-01-28", "date_end": "None", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "526", "kind": "1", "date_begin": "2020-10-23", "date_end": "2015-05-16", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "787", "kind": "1", "date_begin": "2019-08-20", "date_end": "None", "share": "1.02", "depth": 1, "links": []}, {"child": "433", "parent": "782", "kind": "1", "date_begin": "2021-03-11", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "696", "kind": "1", "date_begin": "2021-09-10", "date_end": "2015-05-28", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "957", "kind": "1", "date_begin": "2021-10-09", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "330", "kind": "1", "date_begin": "2022-02-11", "date_end": "2015-01-19", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "137", "kind": "1", "date_begin": "2020-11-08", "date_end": "2016-01-30", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "707", "kind": "1", "date_begin": "2022-10-22", "date_end": "2016-01-05", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "691", "kind": "1", "date_begin": "2022-07-06", "date_end": "2015-11-10", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "824", "kind": "1", "date_begin": "2019-12-22", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "760", "kind": "1", "date_begin": "2019-01-17", "date_end": "2015-07-07", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "37", "kind": "1", "date_begin": "2019-09-06", "date_end": "2016-01-06", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "859", "kind": "1", "date_begin": "2020-07-14", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "910", "kind": "1", "date_begin": "2022-07-07", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "964", "kind": "1", "date_begin": "2021-11-03", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "139", "kind": "1", "date_begin": "2019-01-31", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "652", "kind": "1", "date_begin": "2021-12-23", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "677", "kind": "1", "date_begin": "2021-12-18", "date_end": "2014-11-28", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "307", "kind": "1", "date_begin": "2021-07-15", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "647", "kind": "1", "date_begin": "2019-05-23", "date_end": "2015-04-22", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "251", "kind": "1", "date_begin": "2020-02-23", "date_end": "2015-02-01", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "252", "kind": "1", "date_begin": "2021-06-16", "date_end": "2015-10-30", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "896", "kind": "1", "date_begin": "2022-03-31", "date_end": "2016-02-04", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "16", "kind": "1", "date_begin": "2023-05-24", "date_end": "2015-01-05", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "945", "kind": "1", "date_begin": "2018-05-15", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "510", "kind": "1", "date_begin": "2021-06-06", "date_end": "2015-02-15", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "937", "kind": "1", "date_begin": "2020-03-05", "date_end": "2015-06-26", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "1006", "kind": "1", "date_begin": "2020-10-06", "date_end": "2015-02-17", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "517", "kind": "1", "date_begin": "2019-08-09", "date_end": "2015-11-17", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "55", "kind": "1", "date_begin": "2021-04-25", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "397", "kind": "1", "date_begin": "2020-03-17", "date_end": "2015-08-02", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "604", "kind": "1", "date_begin": "2020-03-29", "date_end": "2015-06-28", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "628", "kind": "1", "date_begin": "2020-01-04", "date_end": "2015-08-17", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "251", "kind": "1", "date_begin": "2023-04-10", "date_end": "2014-11-12", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "636", "kind": "1", "date_begin": "2022-06-03", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "16", "kind": "1", "date_begin": "2019-12-20", "date_end": "2015-03-02", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "189", "kind": "1", "date_begin": "2018-09-12", "date_end": "2014-10-25", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "459", "kind": "1", "date_begin": "2023-02-12", "date_end": "2016-01-18", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "296", "kind": "1", "date_begin": "2020-08-27", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "252", "kind": "1", "date_begin": "2021-04-29", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "472", "kind": "1", "date_begin": "2019-06-06", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "233", "kind": "1", "date_begin": "2020-04-15", "date_end": "2015-12-31", "share": "1.01", "depth": 1, "links": [{"child_id": "73", "object_id": 3, "type": "parent"}]}, {"child": "433", "parent": "976", "kind": "1", "date_begin": "2019-02-17", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "700", "kind": "1", "date_begin": "2018-12-08", "date_end": "2015-02-22", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "211", "kind": "1", "date_begin": "2020-12-16", "date_end": "2014-12-18", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "793", "kind": "1", "date_begin": "2019-05-15", "date_end": "2014-12-17", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "571", "kind": "1", "date_begin": "2018-10-15", "date_end": "2014-11-18", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "85", "kind": "1", "date_begin": "2022-12-28", "date_end": "2015-12-06", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "975", "kind": "1", "date_begin": "2020-02-29", "date_end": "2015-07-18", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "852", "kind": "1", "date_begin": "2018-12-21", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "913", "kind": "1", "date_begin": "2020-10-28", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "845", "kind": "1", "date_begin": "2018-05-22", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "566", "kind": "1", "date_begin": "2021-07-23", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "887", "kind": "1", "date_begin": "2019-02-21", "date_end": "2015-04-04", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "24", "kind": "1", "date_begin": "2022-01-05", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "357", "kind": "1", "date_begin": "2020-03-23", "date_end": "2015-12-21", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "863", "kind": "1", "date_begin": "2020-10-15", "date_end": "2015-11-15", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "719", "kind": "1", "date_begin": "2018-12-08", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "150", "kind": "1", "date_begin": "2023-03-18", "date_end": "None", "share": "1.01", "depth": 1, "links": []}, {"child": "433", "parent": "429", "kind": "1", "date_begin": "2020-08-20", "date_end": "None", "share": "1.0099999999999998", "depth": 1, "links": []}, {"child": "433", "parent": "270", "kind": "1", "date_begin": "2022-07-27", "date_end": "2015-10-07", "share": "1.0099999999999998", "depth": 1, "links": []}]

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

@app.get('/api/front_v1',tags=['front-test'])
async def test_front_v1() -> list:
    return elasticfunc.filling_data(test_data_from_db)

@app.get('/api/front_v2',tags=['front-test'])
async def test_front_v2() -> dict:
    pprint(test_data_from_db)
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
    sort = data['sort'] if 'sort' in data else ""
    return elasticfunc.find_doc_filter(text, regions, okved, sort)


@app.post("/api/find", tags=["main"])
async def get_doc_for_text(data: dict) -> dict:
    index1_indexes = elasticfunc.get_indexes(data['index1']['is_person'], data['index1']['is_company'])
    if len(index1_indexes) <= 0:
        raise HTTPException(status_code=404,detail="Error: Don't select type obj found")
    index1_id = elasticfunc.find_id_doc(data['index1']['data'], index1_indexes)
    if index1_id == "":
        raise HTTPException(status_code=404,detail="Error: First agent don't found")
    index2_id = None
    if 'index2' in data:
        if data['index2'] != "":
            index2_indexes = elasticfunc.get_indexes(data['index2']['is_person'], data['index2']['is_company'])
            if len(index2_indexes) <= 0:
                raise HTTPException(status_code=404,detail="Error: Don't select type obj found")
            index2_id = elasticfunc.find_id_doc(data['index2']['data'], index2_indexes)
            if index2_id == "":
                raise HTTPException(status_code=404,detail="Error: Second agent don't found")

    #TODO: Запрос к postgres
    print(index1_id, index2_id)
    res = None
    if index2_id is not None:
        data = json_loader.generate_json(index1_id, index2_id)
    else:
        pass
    if data != "null":
        nodes, edges = elasticfunc.filling_data_v2(json.loads(data))
        return {'nodes': nodes,
                'edges':edges}
    else:
        raise HTTPException(status_code=404,detail="Not found agent's links")
