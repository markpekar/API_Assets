from decouple import config
from pymongo import MongoClient

def get_database():
    
    CONNECTION_STRING=config("MONGO_STRING")
    client = MongoClient(CONNECTION_STRING)

    db =  client.Assets
    
    return db 