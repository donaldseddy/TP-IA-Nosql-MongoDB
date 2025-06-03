from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
import json


def manage_books():
    books_data=[]
    mongo_manager = MongoManager(MONGO_URI, DB_NAME,"livres")
    
    with open("data\\console_games_clean.json", encoding="utf-8") as f:
            documents = json.load(f)

    for doc in documents:
            if "_id" in doc:
                if isinstance(doc["_id"], dict) and "$oid" in doc["_id"]:
                    doc["_id"] = ObjectId(doc["_id"]["$oid"])
                elif not isinstance(doc["_id"], ObjectId):
                    del doc["_id"]
            books_data.append(doc)  

    if isinstance(books_data, list):
            mongo_manager.create_many_documents(books_data)
    else:
        mongo_manager.create_one_document(books_data)
        print("Documents inserted successfully.")



    # 2. Supprimer un livre par son titre
    delete_result = mongo_manager.collection.delete_one({"title": "1984"})
    print(f"Nombre de livres supprimés (titre = '1984') : {delete_result.deleted_count}")

    # 3. Supprimer tous les livres de J.K. Rowling
    delete_result = mongo_manager.collection.delete_many({"author": "J. K. Rowling"})
    print(f"Nombre de livres supprimés (auteur = J.K. Rowling) : {delete_result.deleted_count}")