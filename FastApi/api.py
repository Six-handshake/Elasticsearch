from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
from typing import Union
import json
import elasticfunc

sys.path.append('/home/serv/elasticsearch/Elasticsearch')
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

test_data_from_db = [{"child": "73", "parent": "16", "kind": "1", "depth": 0}, {"child": "73", "parent": "95", "kind": "1", "depth": 0}, {"child": "73", "parent": "300", "kind": "1", "depth": 0}, {"child": "73", "parent": "38", "kind": "1", "depth": 0}, {"child": "73", "parent": "64", "kind": "1", "depth": 0}, {"child": "73", "parent": "282", "kind": "1", "depth": 0}, {"child": "73", "parent": "133", "kind": "2", "depth": 0}, {"child": "179", "parent": "84", "kind": "1", "depth": 1}, {"child": "179", "parent": "162", "kind": "1", "depth": 1}, {"child": "179", "parent": "223", "kind": "1", "depth": 1}, {"child": "179", "parent": "16", "kind": "1", "depth": 1}, {"child": "179", "parent": "46", "kind": "1", "depth": 1}, {"child": "179", "parent": "238", "kind": "1", "depth": 1}, {"child": "179", "parent": "238", "kind": "1", "depth": 1}, {"child": "179", "parent": "123", "kind": "1", "depth": 1}, {"child": "179", "parent": "74", "kind": "1", "depth": 1}, {"child": "179", "parent": "31", "kind": "1", "depth": 1}, {"child": "179", "parent": "257", "kind": "2", "depth": 1}, {"child": "124", "parent": "70", "kind": "1", "depth": 1}, {"child": "124", "parent": "210", "kind": "1", "depth": 1}, {"child": "124", "parent": "95", "kind": "1", "depth": 1}, {"child": "124", "parent": "220", "kind": "1", "depth": 1}, {"child": "124", "parent": "196", "kind": "1", "depth": 1}, {"child": "124", "parent": "141", "kind": "2", "depth": 1}, {"child": "220", "parent": "246", "kind": "1", "depth": 1}, {"child": "220", "parent": "217", "kind": "1", "depth": 1}, {"child": "220", "parent": "3", "kind": "1", "depth": 1}, {"child": "220", "parent": "20", "kind": "1", "depth": 1}, {"child": "220", "parent": "2", "kind": "1", "depth": 1}, {"child": "220", "parent": "16", "kind": "2", "depth": 1}, {"child": "147", "parent": "224", "kind": "1", "depth": 1}, {"child": "147", "parent": "128", "kind": "1", "depth": 1}, {"child": "147", "parent": "282", "kind": "1", "depth": 1}, {"child": "147", "parent": "10", "kind": "1", "depth": 1}, {"child": "147", "parent": "296", "kind": "1", "depth": 1}, {"child": "147", "parent": "37", "kind": "1", "depth": 1}, {"child": "147", "parent": "82", "kind": "1", "depth": 1}, {"child": "147", "parent": "30", "kind": "1", "depth": 1}, {"child": "147", "parent": "257", "kind": "1", "depth": 1}, {"child": "147", "parent": "12", "kind": "1", "depth": 1}, {"child": "147", "parent": "174", "kind": "1", "depth": 1}, {"child": "147", "parent": "1", "kind": "2", "depth": 1}, {"child": "298", "parent": "193", "kind": "1", "depth": 1}, {"child": "298", "parent": "133", "kind": "1", "depth": 1}, {"child": "298", "parent": "279", "kind": "1", "depth": 1}, {"child": "298", "parent": "139", "kind": "1", "depth": 1}, {"child": "298", "parent": "214", "kind": "1", "depth": 1}, {"child": "298", "parent": "196", "kind": "1", "depth": 1}, {"child": "298", "parent": "74", "kind": "1", "depth": 1}, {"child": "298", "parent": "7", "kind": "2", "depth": 1}, {"child": "76", "parent": "246", "kind": "1", "depth": 2}, {"child": "76", "parent": "74", "kind": "1", "depth": 2}, {"child": "76", "parent": "294", "kind": "1", "depth": 2}, {"child": "76", "parent": "128", "kind": "1", "depth": 2}, {"child": "76", "parent": "196", "kind": "2", "depth": 2}]

@app.get('/api/front_v1',tags=['front-test'])
async def test_front_v1() -> list:
    return elasticfunc.filling_data(test_data_from_db)

@app.get('/api/front_v2',tags=['front-test'])
async def test_front_v2() -> list:
    return elasticfunc.filling_data_v2(test_data_from_db)

@app.get("/api/id/{doc_id}", tags=["main"])
async def get_doc_for_id(doc_id: str, q: Union[str, None] = None) -> dict:
    print("start")
    return elasticfunc.get_data_id(doc_id)


@app.post("/api/find", tags=["main(test)"])
async def get_doc_for_text(data: dict) -> dict:
    index1_id = elasticfunc.find_id_doc(data['index1'])
    index2_id = None
    if 'index2' in data:
        if data['index2'] != "":
            index2_id = elasticfunc.find_id_doc(data['index2'])

    #TODO: Запрос к postgres
    res = None
    if index2_id is not None:
        pass
    else:
        pass

    return elasticfunc.get_data_id(index1_id)