from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.server_api import ServerApi

DB_CONNECTION_ENV_KEY= "MONGO_DB_CONNECTION_STRING_WITH_PASSWORD"
DB_NAME_ENV_KEY = "MONGO_DB_DATABASE_NAME"
COLLECTION_NAME_ENV_KEY = "MONGO_DB_COLLECTION_NAME"

def connect_to_users():
    #env = dotenv_values(".env")
    env = dotenv_values()
    return  MongoClient(env[DB_CONNECTION_ENV_KEY], server_api=ServerApi('1'))[env[DB_NAME_ENV_KEY]][env[COLLECTION_NAME_ENV_KEY]]
