from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
import json

def exo_1():
    game_data = []

    # Créer une BD Exercice avec une collection console_games
    data = MongoManager(MONGO_URI, "exercice", "console_games")
    
    with open("data\\console_games_clean.json", encoding="utf-8") as f:
        documents = json.load(f)

    for doc in documents:
        if "_id" in doc:
            if isinstance(doc["_id"], dict) and "$oid" in doc["_id"]:
                doc["_id"] = ObjectId(doc["_id"]["$oid"])
            elif not isinstance(doc["_id"], ObjectId):
                del doc["_id"]
        game_data.append(doc)  

    if isinstance(game_data, list):
        data.collection.insert_many(game_data)
    else:
        data.collection.insert_one(game_data)

    print("Documents inserted successfully.")

    """print("\n Afficher les jeux 3DS sortis")
    jeux_3DS = data.read_many_documents(game_data)
    for jeu in jeux_3DS:
        print(jeu)
"""
