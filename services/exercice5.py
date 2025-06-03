from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
from datetime import datetime
import json



def creation_collection_magasins():
    magasins_data = []

    # Créer une BD Exercice avec une collection console_games
    data = MongoManager(MONGO_URI, DB_NAME, "magasins")
    
    with open("data\\magasins_clean.json", encoding="utf-8") as f:
        documents = json.load(f)

    for doc in documents:
        if "_id" in doc:
            if isinstance(doc["_id"], dict) and "$oid" in doc["_id"]:
                doc["_id"] = ObjectId(doc["_id"]["$oid"])
            elif not isinstance(doc["_id"], ObjectId):
                del doc["_id"]
        magasins_data.append(doc)  

    if isinstance(magasins_data, list):
        data.create_many_documents(magasins_data) 
    else:
        data.create_one_document(magasins_data)

    print("Documents inserted successfully.")



def ranging_magasins():
    mongo_manager = MongoManager(MONGO_URI, DB_NAME, "magasins")

    magasin_moins_bien_note = mongo_manager.collection.find_one(
    {},
    sort=[("note", 1)]
    )
    magasin_mieux_note = mongo_manager.collection.find_one(
    {},
    sort=[("note", -1)]
    )
    
    magasin_plus_ancien = mongo_manager.collection.find_one(
    {}, 
    sort=[("created_at", 1)]
    )
    magasin_plus_recent = mongo_manager.collection.find_one(
    {},
    sort=[("created_at", -1)]
    )

    print("Le magasin le moins bien noté est : ", magasin_moins_bien_note)
    print("Le magasin le mieux noté est : ", magasin_mieux_note)
    print("Le magasin le plus ancien est : ", magasin_plus_ancien)
    print("Le magasin le plus récent est : ", magasin_plus_recent)
    print("Le magasin le plus ancien est : ", magasin_plus_ancien)


def magasin_note_beetwen_50_80():
    mongo_manager = MongoManager(MONGO_URI, DB_NAME, "magasins")
    magasins = mongo_manager.collection.find(
        {"note": {"$gte": 50, "$lte": 80}}
    )
    for magasin in magasins:
        print(magasin)
    


def magasins_2023():
    start = datetime(2023, 1, 1)
    end = datetime(2024, 1, 1)
    mongo_manager = MongoManager(MONGO_URI, DB_NAME, "magasins")
    magasins = mongo_manager.collection.find(
        {"created_at": {"$gte": start, "$lt": end}}
    )
    for magasin in magasins:
        print(magasin)

def magasins_sans_categorie():
    mongo_manager = MongoManager(MONGO_URI, DB_NAME, "magasins")
    magasins = mongo_manager.collection.find(
        
    {"$or": [{"categories": {"$exists": False}}, {"categories": None}]}
    )
    for magasin in magasins:
        print(magasin)


def magasins_note_sup_75():
    mongo_manager = MongoManager(MONGO_URI, DB_NAME, "magasins")
    magasins = mongo_manager.collection.find(
        {"note": {"$gt": 75}}
    )
    for magasin in magasins:
        print(magasin)


def magasins_votes_50_note_sup_60():
    mongo_manager = MongoManager(MONGO_URI, DB_NAME, "magasins")
    magasins = mongo_manager.collection.find(
        {"$and": [{"votes": {"$gt": 50}}, {"note": {"$gt": 60}}]}
    )
    for magasin in magasins:
        print(magasin)