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


@app.post("/api/todo", tags=["test"])
async def add_test_data(test_data: dict) -> dict:
    todos.append(test_data)
    return {
        "data": {"Test data added."}
    }


@app.get("/api/id/{doc_id}", tags=["main"])
async def get_doc_for_id(doc_id: str, q: Union[str, None] = None) -> dict:
    print("start")
    return elasticfunc.get_data_id(doc_id)


@app.get("/api/find", tags=["main"])
async def get_doc_for_text(data: dict) -> dict:
    return elasticfunc.get_data_text(data['index1'])


@app.get("/api/inn/{inn}", tags=["main"])
async def get_doc_for_inn(inn: str, q: Union[str, None] = None) -> dict:
    return elasticfunc.get_data_test_inn(inn)
