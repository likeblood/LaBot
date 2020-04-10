from datetime import datetime
import logging


from pymongo import MongoClient
from pymongo.collection import ReturnDocument
from bson.binary import Binary


from settings import MONGO_LNK, MONGO_DB


# Enable logging to handle uncaught exceptions
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='LaBot.log')
logger = logging.getLogger(__name__)


client = MongoClient(MONGO_LNK)
db = client.labs
db.lab1.save("/Users/ba/Documents/2_year_study/C++/labs/LAB№3/Lab_1.pdf")

# users_collection = db.users_collection
# print('users collections are created!')


# def create_user_document(user_id, username):
#     """Creates user document in user collection"""
#     user_document = {
#         "user_id": user_id,
#         "username": username,
#         "is_tutor": False,
#         "created_at": datetime.utcnow()
#     }
#     users_collection.insert_one(user_document)


# def get_user_document(user_id):
#     """Tries to get user document from user collection; if it fails returns None"""
#     return users_collection.find_one({"user_id": user_id})