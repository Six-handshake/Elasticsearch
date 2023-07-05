from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

#React connects
origins = [
    "http://localhost:3000",
    "localhost:3000"
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

@app.get("/test_data", tags=["test"])
async def get_test_data() -> dict:
    return { "data": test }