from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI
from services.exercices import exo_1

def main():
    """# Initialize MongoManager with the URI and database name
    mongo_manager = MongoManager(MONGO_URI, DB_NAME)

    # List all databases
    databases = mongo_manager.list_databases()
    print("Databases:")
    for db in databases:
        print(f"- {db}")
    # Close the connection when done
    mongo_manager.close_connection()"""
    exo_1()


if __name__ == "__main__":
    main()
