from pymongo import MongoClient


def setup() -> MongoClient:
    """
    Use this file to set up the database.
    :return:
    """
    uri = "mongodb+srv://4drade:K690ttzVShJzUe57@cluster0.dwjmome.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    return client.books


if __name__ == '__main__':
    # test connection
    db = setup()
    print(db.list_collection_names())
    print(db.books_collection.find_one())
