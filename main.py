from MongoManager import MongoManager
from config.db_config import DB_NAME, MONGO_URI

def main():
    # Initialize MongoManager with the URI and database name
    mongo_manager = MongoManager(MONGO_URI, DB_NAME)

   
    # Close the connection when done
    mongo_manager.close_connection()

if __name__ == "__main__":
    main()
