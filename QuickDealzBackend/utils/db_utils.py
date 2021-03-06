from pymongo import MongoClient
from QuickDealzBackend import application, logger

class Base(object):
    def __init__(self):
        mongo_conn = MongoClient(application.config['MONGO_URI'])
        self.mongo_db = mongo_conn[application.config['DB_NAME']]

    def get(self, collection_name, query):
        try:
            cursor = self.mongo_db[collection_name].find(query)
            count = cursor.count()
            return count, list(cursor)
        except Exception as e:
            print('Exception while getting from MongoDB', e)
            logger.debug('Exception while getting from MongoDB')

    def insert(self, collection_name, documents):
        try:
            collection = self.mongo_db[collection_name]
            print(documents)
            if isinstance(documents, list):
                _id = collection.insert_many(documents).inserted_id
            else:
                _id = collection.insert_one(documents).inserted_id
            return _id
        except Exception as e:
            print('Exception while inserting into MongoDB', e)
            logger.debug('Exception while inserting to MongoDB')

    def update(self, collection_name, query, value):
        try:
            if isinstance(value, list):
                self.mongo_db[collection_name].update_many(query, value)
            else:
                self.mongo_db[collection_name].update_one(query, value)
                logger.debug('Exception while updating MongoDB')
        except Exception as e:
            print('Exception while updating MongoDB', e)
            logger.debug('Exception while updating MongoDB')

    def delete(self, collection_name, query):
        try:
            self.mongo_db[collection_name].update_many(query,
                {"$set": {"meta.is_deleted": True}})
        except Exception as e:
            print('Exception while deleting records in MongoDB', e)
            logger.debug('Exception while deleting records in MongoDB')