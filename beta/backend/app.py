from fastapi import FastAPI, Response
import sys
import os
import uvicorn
from mongo import *
from pymongo import mongo_client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# client = mongo_client.MongoClient(f'mongodb://localhost:29017/')
client = mongo_client.MongoClient('mongodb://host.docker.internal:29017')

print('Conneted to Mongodb....')
mydb = client['test']
collection = mydb['campingjang']

@app.get("/camp/collection")
def collect(response:Response):
    result = list(mongo_query(collection))
    return {"count":len(result),"datas": result}

@app.get("/camp/query")
def query(search:str):
    result = list(mongo_query(collection), search=search)
    return {"count":len(result),"datas": result}

@app.get("/camp/name/{name}")
def resource(name):
    result = mongo_find_one_name(collection, name)
    print(type(result))
    return {"ok":True,"data":result}

@app.get("/camp/row/{row}")
def resource(row):
    result = mongo_find_one_row(collection, int(row))
    print(type(result))
    return {"ok":True,"data":result}

@app.get("/camp/card/collection")
def collect():
    result = list(mongo_card(collection))
    return {"count":len(result),"datas": result}

@app.get("/camp/card/{row}")
def resource_card(row):
    result = mongo_card_one(collection, int(row))
    print(type(result))
    return {"ok":True,"data":result}

@app.delete("/camp")
def delete():
    return

@app.put("/camp")
def update():
    return

@app.post("/camp")
def insert():
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
    print("Server Running Port", 3000, '...')
