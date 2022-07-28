import db
from bson.objectid import ObjectId

class User():
    def __init__(self):
        self.db = db.connect_to_users()
    # TODO
    # Hash password. Don't just store it in plaintext like that
    # This is just for testing purposes
    def new_user(self, email, password):
        user_document = {
            "email": email,
            "password": password,
        }
        self.id = self.db.insert_one(user_document).inserted_id
    def connect_to_user(self, user_id):
            self.id = self.db.find_one({"_id":ObjectId(user_id)})['_id']
    def checkForId(self):
        try:
            if self.id is None:
                raise Exception("You need to connect to the user first via connect_to_user() or new_user()")
        except AttributeError:
                raise Exception("You need to connect to the user first via connect_to_user() or new_user()")
    def save_cal(self, cal):
        self.checkForId()
        self.db.update_one({"_id":self.id}, {"$set": {"cal":cal}})
