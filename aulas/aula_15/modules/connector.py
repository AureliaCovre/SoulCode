from pymongo import MongoClient

def conectar():
    client = MongoClient("mongodb://127.0.0.1:27017/")
    return client['teste']
