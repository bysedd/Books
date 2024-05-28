from datetime import datetime

from utils.constants import FORMAT
from utils.utils import alt_title, validate_string


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
            book.publication_date = publication_date
            book.publisher = publisher if publisher else None
            book.available_copies = available_copies if available_copies else None
            return book
        except ValueError as e:
            print(e)

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        validate_string(title, "Title")
        self.__title = title.title()

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        validate_string(author, "Author")
        self.__author = alt_title(author)

    @property
    def publication_date(self) -> datetime:
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, date: str) -> None:
        publication_date = datetime.strptime(date, FORMAT)
        if publication_date > datetime.now():
            raise ValueError(
                f"Publication date must be less than or equal to {datetime.now().strftime(FORMAT)}"
            )
        self.__publication_date = publication_date.date()

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str) -> None:
        if publisher is None:
            return
        validate_string(publisher, "Publisher")
        self.__publisher = publisher.strip()

    @property
    def available_copies(self) -> int:
        return self.__available_copies

    @available_copies.setter
    def available_copies(self, available_copies: int) -> None:
        if available_copies is None:
            return
        if not isinstance(available_copies, int):
            raise TypeError("Available copies must be an integer")
        if available_copies < 0:
            raise ValueError("Available copies must be greater than or equal to 0")
        self.__available_copies = int(available_copies)
