import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def setup() -> MongoClient:
    """
    Use this file to set up the database.
    :return:
    """
    user, password = os.getenv("MONGO_USER"), os.getenv("MONGO_PASSWORD")
    uri = f"mongodb+srv://{user}:{password}@cluster0.dwjmome.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    return client.books


if __name__ == '__main__':
    # test connection
    db = setup()
    print(db.list_collection_names())
    print(db.books_collection.find_one())
