from app import mongo
from bson.objectid import ObjectId

class UserModel:
    @staticmethod
    def get_all_users():
        return list(mongo.db.users.find())

    @staticmethod
    def get_user(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data)

    @staticmethod
    def update_user(user_id, data):
        return mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete_user(user_id):
        return mongo.db.users.delete_one({"_id": ObjectId(user_id)})
