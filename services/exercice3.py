from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI


def manage_books():
    mongo_manager = MongoManager(DB_NAME, MONGO_URI, "livres")

    
    livres = [
        {"title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "year": 1943, "genre": "Classique"},
        {"title": "Les Misérables", "author": "Victor Hugo", "year": 1862, "genre": "Classique"},
        {"title": "Le Comte de Monte-Cristo", "author": "Alexandre Dumas", "year": 1844, "genre": "Classique"},
        {"title": "Le Rouge et le Noir", "author": "Stendhal", "year": 1830, "genre": "Classique"},
        {"title": "Madame Bovary", "author": "Gustave Flaubert", "year": 1856, "genre": "Classique"},
        {"title": "Germinal", "author": "Émile Zola", "year": 1885, "genre": "Classique"},
        {"title": "Crime et Châtiment", "author": "Fiodor Dostoïevski", "year": 1866, "genre": "Classique"},
        {"title": "Les Trois Mousquetaires", "author": "Alexandre Dumas", "year": 1844, "genre": "Classique"},
        {"title": "À la recherche du temps perdu", "author": "Marcel Proust", "year": 1913, "genre": "Classique"},
        {"title": "L'Étranger", "author": "Albert Camus", "year": 1942, "genre": "Classique"},
        {"title": "Le Vieil Homme et la Mer", "author": "Ernest Hemingway", "year": 1952, "genre": "Classique"},
        {"title": "Le Parfum", "author": "Patrick Süskind", "year": 1985, "genre": "Classique"},
        {"title": "Les Fleurs du mal", "author": "Charles Baudelaire", "year": 1857, "genre": "Poésie"},
        {"title": "Le Cantique des cantiques", "author": "Bible", "year": -1000, "genre": "Poésie"},
        {"title": "Les Contemplations", "author": "Victor Hugo", "year": 1856, "genre": "Poésie"},
        {"title": "Les Illuminations", "author": "Arthur Rimbaud", "year": 1886, "genre": "Poésie"},
        {"title": "Le Dormeur du val", "author": "Arthur Rimbaud", "year": 1870, "genre": "Poésie"},
        {"title": "Demain, dès l’aube", "author": "Victor Hugo", "year": 1856, "genre": "Poésie"},
        {"title": "Harry Potter à l'école des sorciers", "author": "J. K. Rowling", "year": 2001, "genre": "Fantasy"},
        {"title": "Harry Potter et la chambre des secrets", "author": "J. K. Rowling", "year": 2002, "genre": "Fantasy"},
        {"title": "Le Seigneur des Anneaux", "author": "J. R. R. Tolkien", "year": 1954, "genre": "Fantasy"},
        {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Science Fiction"},
        {"title": "Le Meilleur des mondes", "author": "Aldous Huxley", "year": 1932, "genre": "Science Fiction"},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "genre": "Science Fiction"},
        {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genre": "Science Fiction"},
        {"title": "Le Hobbit", "author": "J. R. R. Tolkien", "year": 1937, "genre": "Fantasy"},
        {"title": "Les Misérables", "author": "Victor Hugo", "year": 1862, "genre": "Classique"},
        {"title": "Germinal", "author": "Émile Zola", "year": 1885, "genre": "Classique"},
        {"title": "Madame Bovary", "author": "Gustave Flaubert", "year": 1856, "genre": "Classique"},
        {"title": "Le Rouge et le Noir", "author": "Stendhal", "year": 1830, "genre": "Classique"},
        {"title": "Crime et Châtiment", "author": "Fiodor Dostoïevski", "year": 1866, "genre": "Classique"},
        {"title": "Le Comte de Monte-Cristo", "author": "Alexandre Dumas", "year": 1844, "genre": "Classique"},
        {"title": "Les Trois Mousquetaires", "author": "Alexandre Dumas", "year": 1844, "genre": "Classique"},
        {"title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "year": 1943, "genre": "Classique"},
        {"title": "L'Étranger", "author": "Albert Camus", "year": 1942, "genre": "Classique"},
        {"title": "À la recherche du temps perdu", "author": "Marcel Proust", "year": 1913, "genre": "Classique"},
        {"title": "Le Vieil Homme et la Mer", "author": "Ernest Hemingway", "year": 1952, "genre": "Classique"},
        {"title": "Le Parfum", "author": "Patrick Süskind", "year": 1985, "genre": "Classique"},
        {"title": "Les Fleurs du mal", "author": "Charles Baudelaire", "year": 1857, "genre": "Poésie"},
        {"title": "Le Cantique des cantiques", "author": "Bible", "year": -1000, "genre": "Poésie"},
        {"title": "Les Contemplations", "author": "Victor Hugo", "year": 1856, "genre": "Poésie"},
        {"title": "Les Illuminations", "author": "Arthur Rimbaud", "year": 1886, "genre": "Poésie"},
        {"title": "Le Dormeur du val", "author": "Arthur Rimbaud", "year": 1870, "genre": "Poésie"},
        {"title": "Demain, dès l’aube", "author": "Victor Hugo", "year": 1856, "genre": "Poésie"},
        
    ]    

    try:
        mongo_manager.collection.insert_many(livres)
        print("Livres ajoutés avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout des livres : {e}")


    # 2. Supprimer un livre par son titre
    delete_result = mongo_manager.collection.delete_one({"title": "1984"})
    print(f"Nombre de livres supprimés (titre = '1984') : {delete_result.deleted_count}")

    # 3. Supprimer tous les livres de J.K. Rowling
    delete_result = mongo_manager.collection.delete_many({"author": "J. K. Rowling"})
    print(f"Nombre de livres supprimés (auteur = J.K. Rowling) : {delete_result.deleted_count}")