from datetime import datetime
from textwrap import dedent

from scripts.base_db import BaseDB
from utils.constants import FORMAT
from utils.logger import log
from utils.utils import validate_string


class Book:
    def __init__(
        self,
    ):
        self.__title: str = None
        self.__author: str = None
        self.__publication_date: datetime = None
        self.__publisher: str = None
        self.__available_copies: int = None

    @staticmethod
    def create_book():
        try:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_date = input("Enter publication date (yyyy-MM-DD): ")
            publisher = input("Enter book publisher: ")
            available_copies = input("Enter number of available copies: ")

            book = Book()
            book.title = title
            book.author = author
            book.publication_date = publication_date if publication_date else None
            book.publisher = publisher if publisher else None
            book.available_copies = available_copies if available_copies else None
            return book
        except ValueError:
            print("Invalid input. Please try again.")

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        validate_string(title, "Title")
        self.__title = title

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        validate_string(author, "Author")
        self.__author = author

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str) -> None:
        validate_string(publisher, "Publisher")
        self.__publisher = publisher.strip()

    @property
    def available_copies(self) -> int:
        return self.__available_copies

    @available_copies.setter
    def available_copies(self, available_copies: int) -> None:
        if not isinstance(available_copies, int):
            raise TypeError("Available copies must be an integer")
        if available_copies < 0:
            raise ValueError("Available copies must be greater than or equal to 0")
        self.__available_copies = int(available_copies)

    @property
    def publication_date(self) -> str | datetime:
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, publication_date: str | datetime) -> None:
        if not isinstance(publication_date, datetime):
            publication_date = datetime.strptime(publication_date, FORMAT)
        if publication_date > datetime.now():
            raise ValueError(
                f"Publication date must be less than or equal to {datetime.now().strftime(FORMAT)}"
            )
        self.__publication_date = publication_date

    def __str__(self):
        return dedent(
            f"""\
            Title: {self.__title}
            Author: {self.__author}
            Publication date: {self.__publication_date}
            Publisher: {self.__publisher}
            Available copies: {self.__available_copies}
            """
        ).strip()


class BooksDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.c.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_date DATE,
                publisher TEXT,
                available_copies INTEGER
            )
            """
        )

    def create(self, obj: Book) -> None:
        publication_date = obj.publication_date
        if not isinstance(obj.publication_date, datetime):
            publication_date = datetime.strptime(obj.publication_date, FORMAT)
        self.c.execute(
            f"""
            INSERT INTO {self.table_name} (title, author, publication_date, publisher, available_copies)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                obj.title,
                obj.author,
                publication_date,
                obj.publisher,
                obj.available_copies,
            ),
        )
        self.conn.commit()
        log(f"Book {self.book.title} added successfully")

    def update(self, primary_key: int, obj: Book) -> None:
        super().update(primary_key, obj)
        self.c.execute(
            f"""
            UPDATE {self.table_name}
            SET title = ?, author = ?, publication_date = ?, publisher = ?, available_copies = ?
            WHERE id = ?
            """,
            (
                obj.title,
                obj.author,
                obj.publication_date,
                obj.publisher,
                obj.available_copies,
                primary_key,
            ),
        )
        self.conn.commit()
        log(f"Book '{obj.title}' updated successfully")

    @property
    def table_name(self) -> str:
        return "books"
