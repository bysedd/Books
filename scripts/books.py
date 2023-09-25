import random
from datetime import datetime
import uuid
from faker import Faker

from mongo.books import get_random_title


class Books:
    """
    A class to represent a book.
    """

    def __init__(self):
        """
        Constructor to create a new book record with random attributes.
        """
        faker = Faker()

        self.book_id = uuid.uuid4()
        self.title = get_random_title()
        self.author = faker.name()
        self.publisher = faker.company()
        self.available_copies = random.randint(0, 100)
        self.publication_date = faker.date_between(start_date='-30y', end_date='today')
        self.year = self.publication_date.year

    def set_title(self, title: str):
        """
        Set the title of the book.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.title = title

    def set_author(self, author):
        """
        Set the author of the book.
        """
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        self.author = author

    def set_year(self, year):
        """
        Set the year to complete the writing of the book.
        """
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")

        if year < 0 or year > datetime.now().year:
            raise ValueError(f"Year must be between 0 and {datetime.now().year}")
        self.year = year

    def set_publisher(self, publisher: str):
        """
        Set the publisher of the book.
        """
        if not isinstance(publisher, str):
            raise TypeError("Publisher must be a string")

        self.publisher = publisher

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
        self.available_copies = available_copies

    def set_publication_date(self, publication_date: datetime):
        """
        Set the publication date of the book.
        """
        if not isinstance(publication_date, datetime):
            raise TypeError("Publication date must be a datetime object")

        self.publication_date = publication_date

    def get_title(self):
        """
        Get the title of the book.
        """
        return self.title

    def get_author(self):
        """
        Get the author of the book.
        """
        return self.author

    def get_year(self):
        """
        Get the publication year of the book.
        """
        return self.year

    def get_publisher(self):
        """
        Get the publisher of the book.
        """
        return self.publisher

    def get_available_copies(self):
        """
        Returns the amount enabled copies of a book.

        :return: The amount enabled copies of the book.
        """
        return self.available_copies

    def get_publication_date(self):
        """
        Get the publication date of the book.
        """
        return self.publication_date

    def __str__(self):
        return f"""Title: {self.title}
Author: {self.author}
Year: {self.year}
Publisher: {self.publisher}
Available copies: {self.available_copies}
Publication date: {self.publication_date}
""".strip()


# Example usage:
if __name__ == "__main__":
    book = Books()

    print(book)
