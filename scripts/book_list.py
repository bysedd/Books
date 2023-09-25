from datetime import datetime
from typing import Dict

from scripts.books import Books
from utils.logger import log


class BookList:
    """
    Offers capacity for storing, searching for, and deleting Books instances.
    """

    def __init__(self):
        """
        Create a new dictionary collection for Book instances.
        """
        self.book_collection: Dict[int, Books] = {}

    def store_book(self, book_: Books):
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


if __name__ == '__main__':
    book = Books()
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
