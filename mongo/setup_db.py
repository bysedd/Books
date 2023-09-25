from pymongo import MongoClient


def setup() -> MongoClient:
    """
    Use this file to set up the database.
    :return:
    """
    uri = "mongodb+srv://4drade:dede9895@cluster0.dwjmome.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    return client.books
