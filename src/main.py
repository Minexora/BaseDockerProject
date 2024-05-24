import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() 

mongo_user = os.getenv('MONGO_USER')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_database = os.getenv('MONGO_DATABASE')

print("mongo_database:" , mongo_database)
print("mongo_user:" , mongo_user)
print("mongo_password:" , mongo_password)


# uri = f"mongodb://{mongo_user}:{mongo_password}@mongoDB:27017/{mongo_database}"
uri = f"mongodb://{mongo_user}:{mongo_password}@mongoDB:27017/"

client = MongoClient(uri)

def list_collections():
    db = client[mongo_database]
    collections = db.list_collection_names()
    print('Collections:')
    for collection in collections:
        print(collection)

list_collections()
client.close()