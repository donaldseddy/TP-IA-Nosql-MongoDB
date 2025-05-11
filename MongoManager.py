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

    @property
    def db(self) -> Database:
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        return self.__db
    
    @db.setter
    def db(self, db_name: str):
        self.__db = self.__client[db_name]
    # réaffectation obligatoire de la collection car changement de database
        if self.__collection is not None:
            self.collection = self.__collection.name # .name car collection est un objet

    @property
    def collection(self) -> Collection:
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        return self.__collection
    
    @collection.setter
    def collection(self, coll_name: str):
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        self.__collection = self.__db[coll_name]

    def list_databases(self):
        try:
            return self.__client.list_database_names()
        except Exception as e:
            raise Exception("Unable to list databases due to the following error: ", e)
        
    def list_collections(self):
        if self.__db is None:
            raise Exception("Database not initialized. Please provide a database name.")
        try:
            return self.__db.list_collection_names()
        except Exception as e:
            raise Exception("Unable to list collections due to the following error: ", e)
        


    def create_one_document(self, document):
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        try:
            result = self.__collection.insert_one(document)
            return result.inserted_id
        except Exception as e:
            raise Exception("Unable to create document due to the following error: ", e)
        

    def create_many_documents(self, documents):
        if self.__collection is None:
            raise Exception("Collection not initialized. Please provide a collection name.")
        try:
            result = self.__collection.insert_many(documents)
            return result.inserted_ids
        except Exception as e:
            raise Exception("Unable to create documents due to the following error: ", e)
        
    def update_one_document(self, query: dict, new_values: dict):
        try:
            update_result = self.collection.update_one(query, new_values)
            return {
            "acknowledged": update_result.acknowledged,
            "insertedId": update_result.upserted_id,
            "matchedCount": update_result.matched_count,
            "modifiedCount": update_result.modified_count,
            }
        except Exception as e:
            raise Exception("Unable to update the document due to the following error:", e)

    def update_many_documents(self, query: dict, new_values: dict):
        try:
            update_result = self.collection.update_many(query, new_values)
            return {
            "acknowledged": update_result.acknowledged,
            "insertedId": update_result.upserted_id,
            "matchedCount": update_result.matched_count,
            "modifiedCount": update_result.modified_count,
            }
        except Exception as e:
            raise Exception("Unable to update the documents due to the following error:", e)
        

    def read_one_document(self, query: dict):
        try:
            document = self.collection.find_one(query)
            return document
        except Exception as e:
            raise Exception("Unable to read the document due to the following error:", e)
        
    def read_many_documents(self, query: dict):
        try:
            documents = self.collection.find(query)
            return list(documents)
        except Exception as e:
            raise Exception("Unable to read the documents due to the following error:", e)
        
    def read_sorted_documents(self, query: dict, sort_by: str, order: int):
        try:
            documents = self.collection.find(query).sort(sort_by, order)
            return list(documents)
        except Exception as e:
            raise Exception("Unable to read the sorted documents due to the following error:", e)
        

    def delete_one_document(self, query: dict):
        try:
            delete_result = self.collection.delete_one(query)
            return {
            "acknowledged": delete_result.acknowledged,
            "deletedCount": delete_result.deleted_count,
            }
        except Exception as e:
            raise Exception("Unable to delete the document due to the following error:", e)
        
    
    def delete_many_documents(self, query: dict):
        try:
            delete_result = self.collection.delete_many(query)
            return {
            "acknowledged": delete_result.acknowledged,
            "deletedCount": delete_result.deleted_count,
            }
        except Exception as e:
            raise Exception("Unable to delete the documents due to the following error:", e)