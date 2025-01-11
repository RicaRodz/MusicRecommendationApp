from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb://mongodb:27017")
db = client["mydatabase"]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}
