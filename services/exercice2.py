from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from bson import ObjectId
import json


"Créez une collection livre :( titre : string unique auteur : string non vide année : int, supérieur à 1900 genre : string optionnel )"

def create_book_collection():
    
        mongo_manager = MongoManager(DB_NAME, MONGO_URI)
        # Define the schema for the book collection
        book_schema = {
            "title": {"type": "string", "unique": True},
            "author": {"type": "string", "required": True},
            "year": {"type": "int", "min": 1900},
            "genre": {"type": "string", "optional": True}
        }

        # Create the collection with the defined schema
        mongo_manager.create_collection("livres", book_schema)
        print("Collection 'livres' created with the specified schema.")
        mongo_manager.close_connection()
        
def add_book():
        
    books = [
        {"title": "Harry Potter à l'école des sorciers", "author": "J. K. Rowling", "year": 2001, "genre": "Fantasy"},
        {"title": "Harry Potter et la chambre des secrets", "author": "J. K. Rowling", "year": 2002, "genre": "Fantasy"},
        {"title": "Livre vieux", "author": "Auteur inconnu", "year": 1800},
        {"title": "Harry Potter à l'école des sorciers", "author": "Copycat", "year": 2012, "genre": "Fantasy"}
    ]

    mongo_manager = MongoManager(DB_NAME, MONGO_URI, "livres")

    for book in books:
        try:
            mongo_manager.collection.insert_one(book)
            print(f"Livre inséré : {book['title']}")
        except Exception as e:
            print(f"Erreur pour '{book['title']}' : {e}")
