# Import the Library
from typing import *
from fastapi import FastAPI
from db import connect_mongo
import os

app = FastAPI()

# Load enviroment Variables
db_name = 'pass-safe'
uri:str = os.getenv('MONGO_URI')

# Conecct MongoDB
mongo_info: Dict[str, Any] = connect_mongo(uri, db_name)

# Extract the collection is info the Mongo_info
client:str = mongo_info["client"]
db:str = mongo_info["db"]

# Test Connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)