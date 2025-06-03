from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
import json





def creation_collection_city():
    city_data = []

    # Créer une BD Exercice avec une collection console_games
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    
    with open("data\\city.json", encoding="utf-8") as f:
        documents = json.load(f)

    for doc in documents:
        if "_id" in doc:
            if isinstance(doc["_id"], dict) and "$oid" in doc["_id"]:
                doc["_id"] = ObjectId(doc["_id"]["$oid"])
            elif not isinstance(doc["_id"], ObjectId):
                del doc["_id"]
        city_data.append(doc)  

    if isinstance(city_data, list):
        data.create_many_documents(city_data) 
    else:
        data.create_one_document(city_data)

    print("Documents inserted successfully.")


def update_city_name():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document(
        {"name": "Paris 15"},
        {"$set": {"name": "Paris 15ème arrondissement"}}
    )
    print("City name updated successfully.")


def update_city_coordinates():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document(
        {"name": "Lyon"},
        {"$set": {"coordinates": [45.7640, 4.8357]}}
    )
    print("City coordinates updated successfully.")

def update_city_population():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document(
        {"name": "Lyon"},
        {"$set": {"population": 500000}}
    )
    print("City population updated successfully.")


def update_city_resquest_tag():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document({},
    {"$addToSet": {"tags": {"$each": ["historique", "touristique"]}}}
    )
    print("City request_tag updated successfully.")


def update_city_resquest_delete_tag():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document({},
    {"$pull": {"tags": "historique"}}
    )
    print("City request_tag updated successfully.")


def update_city_resquest_delete_fist_thing_tag():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document({"city_name": "Bourges"},
    {"$pop": {"tags": -1}}
    )
    print("City request_tag updated successfully.")


def update_city_resquest_delete_all_tag():
    data = MongoManager(MONGO_URI, DB_NAME, "city")
    data.update_one_document({"city_name": "Bourges"},
    {"$unset": {"tags": ""}}
    )
    print("City request_tag updated successfully.")