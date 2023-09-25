import random
from datetime import datetime
from typing import Dict, Any

from faker import Faker

from mongo.books import get_random_title


class Books:
    """
    A class to represent a book.
    """
    book_id = 1

    def __init__(self):
        """
        Constructor to create a new book record with random attributes.
        """
        faker = Faker()

        self.book_id = Books.book_id
        Books.book_id += 1
        self.__title = get_random_title()
        self.__author = faker.name()
        self.__publisher = faker.company()
        self.__available_copies = random.randint(0, 100)
        self.__publication_date = faker.date_between(start_date='-30y', end_date='today')
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
            raise ValueError(
                f"Number of available copies must be greater than 0"
            )
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

    def get_publication_date(self):
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
            "publication_date": self.get_publication_date().strftime("%Y-%m-%d")
        }


# Example usage:
if __name__ == "__main__":
    book = Books()
    print(book)
