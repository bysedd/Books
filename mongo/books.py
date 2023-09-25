from mongo.setup_db import setup
from utils.logger import func_log
from utils.constants import BASE_DIR

from typing import Generator, Any


db = setup()
books_collection = db.books_collection


def get_random_title() -> str:
    """
    Generate a random title from the book collection.

    :return: The random title generated from the book collection.
    """
    global books_collection
    random_book = books_collection.aggregate([{"$sample": {"size": 1}}])
    for book_ in random_book:
        return book_['title']


@func_log
def add_to_db(books_: Generator[str, Any, None], /) -> None:
    """
    Add books to the mongodb collection.

    :param books_: A generator of book titles.
    """
    for book_ in books_:
        # Check if the book already exists in the database
        if not books_collection.find_one({"title": book_}):
            books_collection.insert_one(book_)


if __name__ == '__main__':
    with open(BASE_DIR / "data" / "books.txt", "r", encoding="utf-8") as f:
        books = (book_.strip() for book_ in f.readlines())

    # add_to_db(books)
    print(f"Random book title: {get_random_title()}")
