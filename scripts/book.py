import random
from datetime import datetime
from typing import Any
from typing import Dict
from typing import Generator

from faker import Faker

from utils.constants import BASE_DIR
from utils.logger import log


def get_random_title() -> str:
    """
    Generate a random title from the book collection.

    :return: The random title generated from the book collection.
    """
    return random.choice([*get_all_books()])


class Book:
    """
    A class to represent a book.
    """

    book_id = 1

    def __init__(self):
        """
        Constructor to create a new book record with random attributes.
        """
        faker = Faker()

        self.book_id = Book.book_id
        Book.book_id += 1
        self.__title = get_random_title()
        self.__author = faker.name()
        self.__publisher = faker.company()
        self.__available_copies = random.randint(0, 100)
        self.__publication_date = faker.date_between(
            start_date="-30y", end_date="today"
        )
        self.__year = self.get_publication_date().year

    def set_title(self, title: str):
        """
        Set the title of the book.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.__title = title

    def set_author(self, author):
        """
        Set the author of the book.
        """
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        self.__author = author

    def set_year(self, year):
        """
        Set the year to complete the writing of the book.
        """
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")

        if year < 0 or year > datetime.now().year:
            raise ValueError(f"Year must be between 0 and {datetime.now().year}")
        self.__year = year

    def set_publisher(self, publisher: str):
        """
        Set the publisher of the book.
        """
        if not isinstance(publisher, str):
            raise TypeError("Publisher must be a string")

        self.__publisher = publisher

    def set_available_copies(self, available_copies: int):
        """
        Set the amount copies enabled.
        """
        if not isinstance(available_copies, int):
            raise TypeError("Available copies must be an integer")

        if available_copies < 0:
            raise ValueError(f"Number of available copies must be greater than 0")
        self.__available_copies = available_copies

    def set_publication_date(self, publication_date: datetime):
        """
        Set the publication date of the book.
        """
        if not isinstance(publication_date, datetime):
            raise TypeError("Publication date must be a datetime object")

        self.__publication_date = publication_date

    def get_title(self):
        """
        Get the title of the book.
        """
        return self.__title

    def get_author(self):
        """
        Get the author of the book.
        """
        return self.__author

    def get_year(self):
        """
        Get the publication year of the book.
        """
        return self.__year

    def get_publisher(self):
        """
        Get the publisher of the book.
        """
        return self.__publisher

    def get_available_copies(self):
        """
        Returns the amount enabled copies of a book.

        :return: The amount enabled copies of the book.
        """
        return self.__available_copies

    def get_publication_date(self) -> datetime:
        """
        Get the publication date of the book.
        """
        return self.__publication_date

    def __str__(self):
        return f"""Book ID: {self.book_id}
Title: {self.__title}
Author: {self.__author}
Year: {self.__year}
Publisher: {self.__publisher}
Available copies: {self.__available_copies}
Publication date: {self.__publication_date.strftime("%Y-%m-%d")}
""".strip()

    def json(self) -> Dict[str, Any]:
        return {
            "book_id": self.book_id,
            "title": self.get_title(),
            "author": self.get_author(),
            "year": self.get_year(),
            "publisher": self.get_publisher(),
            "available_copies": self.get_available_copies(),
            "publication_date": self.get_publication_date().strftime("%Y-%m-%d"),
        }


def get_all_books() -> Generator[str, Any, None]:
    """
    Returns all books stored in the collection.

    :return: All books
    """
    with open(BASE_DIR / "data" / "books.txt", "r", encoding="utf-8") as f:
        books = (book_.strip() for book_ in f.readlines())
    return books


class BookList:
    """
    Offers capacity for storing, searching for, and deleting Books instances.
    """

    def __init__(self):
        """
        Create a new dictionary collection for Book instances.
        """
        self.book_collection: Dict[int, Book] = {}

    def store_book(self, book_: Book):
        """
        Store a Book instance in the collection.

        :param book_: The Book instance to store.
        """
        try:
            # Check if the book is already stored
            if book_.book_id in self.book_collection:
                log(f"Book with title '{book_.get_title()}' already stored")
                return

            self.book_collection[book_.book_id] = book_
            log(f"Book with title '{book_.get_title()}' stored successfully")
        except Exception as ex:
            log(f"Failed to store book {book_.book_id} due to {ex}")

    def search_book(self, key: str, value: str | datetime) -> None:
        """
        Examines the book collection for a specific attribute value.

        :param key: The attribute for search, for example, 'publication_date: datetime(yyyy-mm-dd)'.
        :param value: The attribute's expected value.
        :return: Returns a list of Book instances, which match the search criteria.
        """
        try:
            for _, book_ in self.book_collection.items():
                if key == "publication_date" and book_.get_publication_date() == value:
                    print(book_)
                    break

                if book_.json().get(key) == value:
                    print(book_)
                    break
            else:
                log(f"Book with {key=} {value=} not found")
        except AttributeError:
            log(f"Book object don't have attribute {key}")
        except Exception as ex:
            log(f"An error occurred: {ex}")

    def remove_book(self, title_: str) -> None:
        """
        Remove a book from the collection identified by its title.

        :param title_: The title of the intended removed book.
        """
        try:
            for book_id, book_ in self.book_collection.items():
                if book_.get_title() == title_:
                    del self.book_collection[book_id]
                    log(f"Book with title '{title_}' removed successfully")
                    break
            else:
                log(f"Book with title '{title_}' doesn't exist")
        except Exception as ex:
            log(f"Failed to remove title '{title_}' due to {ex}")

    def total_books(self):
        """
        The total number of books stored in the collection.

        :return: Total amount books
        """
        return len(self.book_collection)

    def __repr__(self):
        return f"{type(self).__name__}({self.__dict__!r})"


# Example usage:
if __name__ == "__main__":
    book = Book()
    print(book)
    print()

    book.set_title("The Hobbit")
    book.set_author("Tolkien")
    book.set_publisher("Allen")
    book.set_publication_date(datetime(1998, 9, 21))

    book_list = BookList()

    book_list.store_book(book)

    # book_list.search_book("title", "The Hobbit")                      ✅
    # book_list.search_book("author", "Tolkien")                        ✅
    # book_list.search_book("publisher", "Allen")                       ✅
    # book_list.search_book("publication_date", datetime(1998, 9, 21))  ✅

    book_list.remove_book("The Hobbit")
