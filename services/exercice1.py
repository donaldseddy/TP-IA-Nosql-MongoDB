from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
import json

def creation_bd_initial():
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
        data.create_one_document(game_data)
    else:
        data.create_many_documents(game_data)

    print("Documents inserted successfully.")

def afffichage_jeux_3ds():
    data= MongoManager(MONGO_URI, DB_NAME, "console_games")
    # Afficher les jeux 3DS
    jeux_3ds = data.read_many_documents({"Platform": "3DS"})

    for jeu in jeux_3ds:
        print(f"- {jeu.get('Name')} ({jeu.get('Year')})")
        print(f"  Genre       : {jeu.get('Genre')}")
        print(f"  Publisher   : {jeu.get('Publisher')}")
        print(f"  NA Sales    : {jeu.get('NA_Sales')} M")
        print(f"  EU Sales    : {jeu.get('EU_Sales')} M")
        print(f"  JP Sales    : {jeu.get('JP_Sales')} M")
        print(f"  Other Sales : {jeu.get('Other_Sales')} M")
        print(f"  Global      : {jeu.get('Global_Sales')} M\n")


def affichage_jeux_3ds_2011():
    data= MongoManager(MONGO_URI, DB_NAME, "console_games")

    
    dictionnaire = {
        "Platform": "3DS",
        "Year": "2011" 
    }
    jeux_3ds_2011 = data.read_many_documents(dictionnaire)

    for jeu in jeux_3ds_2011:
        print(f"- {jeu.get('Name')} ({jeu.get('Year')})")
        print(f"  Genre       : {jeu.get('Genre')}")
        print(f"  Publisher   : {jeu.get('Publisher')}")
        print(f"  Global Sales: {jeu.get('Global_Sales')} M\n")



def affichage_jeux_3ds_2011_essential():
    data= MongoManager(MONGO_URI, DB_NAME, "console_games")

    dictionnaire = {
        "Platform": "3DS",
        "Year": "2011" 
    }
    jeux_3ds_2011 = data.read_many_documents(dictionnaire)

    for jeu in jeux_3ds_2011:
        print(f"- {jeu.get('Name')}")
        print(f"  Global Sales: {jeu.get('Global_Sales')} M\n")

    
def affichage_jeux_3ds_2011_best_3():
    data= MongoManager(MONGO_URI, DB_NAME, "console_games")

    dictionnaire = {
        "Platform": "3DS",
        "Year": "2011" 
    }
    jeux_3ds_2011 = data.read_sorted_documents(dictionnaire, "Global_Sales", -1)

    print("Top 3 des jeux 3DS sortis en 2011 par ventes globales :\n")
    for jeu in jeux_3ds_2011[:3]:
        print(f"- {jeu.get('Name')}")
        print(f"  Global Sales: {jeu.get('Global_Sales')} M\n")

    