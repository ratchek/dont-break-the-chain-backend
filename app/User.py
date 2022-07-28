from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.server_api import ServerApi

DB_CONNECTION_ENV_KEY= "MONGO_DB_CONNECTION_STRING_WITH_PASSWORD"
class User():
    def __init__(self):
        config = dotenv_values(".env")
        self.client = MongoClient(config[DB_CONNECTION_ENV_KEY], server_api=ServerApi('1'))

    # TODO
    # Hash password. Don't just store it in plaintext like that
    # This is just for testing purposes
    def new_user(self, email, password):
        user_document = {
            "email": email,
            "password": password,
        }
        self.client.test.users.insert_one(user_document)


