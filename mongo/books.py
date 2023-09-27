from typing import Generator, Any

from mongo.mongodb import setup
from scripts.book import get_random_title, get_all_books
from utils.logger import func_log

db = setup()
books_collection = db.books_collection


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
    books = get_all_books()
    # add_to_db(books)

    print(f"Random book title: {get_random_title()}")
