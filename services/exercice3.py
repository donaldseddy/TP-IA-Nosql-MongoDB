from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
import json


def manage_books():
    manage_books = MongoManager(MONGO_URI, DB_NAME, "livres")
    # 2. Supprimer un livre par son titre
    delete_result = manage_books.collection.delete_one({"title": "1984"})
    print(f"Nombre de livres supprimés (titre = '1984') : {delete_result.deleted_count}")

    # 3. Supprimer tous les livres de J.K. Rowling
    delete_result = manage_books.collection.delete_many({"author": "J. K. Rowling"})
    print(f"Nombre de livres supprimés (auteur = J.K. Rowling) : {delete_result.deleted_count}")