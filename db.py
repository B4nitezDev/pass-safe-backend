from pymongo import MongoClient # type: ignore
from pymongo.server_api import ServerApi

def connect_mongo(url: str, db_name: str):
    client = MongoClient(url,server_api=ServerApi('1'))
    db = client[db_name]
    #collection = db[collection_name]

    return {
        "client": client,
        "db": db,
    }
