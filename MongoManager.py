from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoManager:
    def __init__(self, uri: str, db_name: str=None, coll_name: str=None):
        self.__client = MongoClient(uri, server_api=ServerApi('1'), tls=True)
        try:
            ping = self.__client.admin.command({'ping': 1})
            print(f"Pinged your deployment: {ping}. You successfully connected to MongoDB!")
        except Exception as e:
            raise Exception("Unable to connect to MongoDB due to the following error: ", e)
        self.__db = None
        self.__collection = None
        if db_name is not None:
            self.__db: Database = self.__client[db_name]
        if coll_name is not None:
            self.__collection: Collection = self.__db[coll_name]
    
    def close_connection(self):
            self.__client.close()
            print("Connection closed.")