from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://admin:1HRx7hisZ9iduaaW@cluster0.iiuqp9u.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    db =  client.Assets

    return db 