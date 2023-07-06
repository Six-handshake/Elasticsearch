from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Elasticsearch import  elasticfunc
from typing import Union
import json

app = FastAPI()

#React connects
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

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": " Hello World"}

@app.post("/test_data", tags=["test"])
async def add_test_data(test_data: dict) -> dict:
    test.append(test_data)
    return {
        "data": { "Test data added." }
    }

@app.get("/test_data/{doc_id}", tags=["test"])
async def get_test_data(doc_id : str) -> dict:
    return { "data": test }

@app.get("/id/{doc_id}",tags=["main"])
async def get_doc_for_id(doc_id : str, q: Union[str, None] = None) -> dict:
    return elasticfunc.get_data_id(doc_id)

@app.get("/test",tags=["main"])
async def get_doc_for_text(q: Union[str, None] = None) -> dict:
    print(q)
    return elasticfunc.get_data_text("erewr")

@app.get("/inn/{inn}",tags=["main"])
async def get_doc_for_inn(inn : str, q: Union[str, None] = None) -> dict:
    return elasticfunc.get_data_test_inn(inn)
