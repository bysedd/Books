from datetime import datetime, timedelta
from typing import Dict

from scripts.book import Book, get_all_books
from scripts.user import User, UserList, generate_user
from utils.logger import log


class Loans:
    """
    The Loans class is responsible for managing loans of books to users.
    """

    def __init__(self):
        self.book_list = list(get_all_books())
        self.user_list = []
        self.loan_records = {}

    def borrow_book(self, user: User, book: Book) -> None:
        if not isinstance(user, User) or not isinstance(book, Book):
            log(
                "Invalid argument types. user_ must be an instance of User and book must be an instance of Books."
            )
            return

        if book.get_title() not in self.book_list:
            log("The book is not available")
            return

        if user.get_username() in self.loan_records:
            self.loan_records[user.get_username()].append(book)
        else:
            self.loan_records[user.get_username()] = [book]

        self.book_list.remove(book.get_title())
        self.user_list.append(user)

        log(f"User '{user.get_username()}' borrowed book '{book.get_title()}'")

    def return_book(self, user: User, book: Book) -> None:
        if not isinstance(user, User) or not isinstance(book, Book):
            log(
                "Invalid argument types. user_ must be an instance of User and book must be an instance of Books."
            )
            return

        if (
            user.get_username() in self.loan_records
            and book in self.loan_records[user.get_username()]
        ):
            self.loan_records[user.get_username()].remove(book)
            self.book_list.append(book.get_title())

            if not self.loan_records[user.get_username()]:
                self.user_list.remove(user.get_username())

            log(f"User '{user.get_username()}' returned book '{book.get_title()}'")

    def count_borrowed_books(self, user: User) -> None | int:
        if not isinstance(user, User):
            log("Invalid argument type, user_ must be an instance of User.")
            return

        try:
            borrowed_books = len(self.loan_records[user.get_username()])
            log(f"User '{user.get_username()}' has borrowed {borrowed_books} book(s)")
        except KeyError:
            log(f"User '{user.get_username()}' has not borrowed any books yet")
            return 0

    def overdue_books(self, users_list: UserList) -> Dict[str, Dict[str, str]]:
        today = datetime.now()
        overdue_books = {}
        for username, borrowed_books in self.loan_records.items():
            for book in borrowed_books:
                due_date = datetime.strptime(str(today.date()), "%Y-%m-%d") + timedelta(
                    days=30
                )
                # print(f"{today.date()} | {due_date.date()}")
                if due_date < today:
                    user = users_list.user_collection.get(username)
                    if user:
                        if username not in overdue_books:
                            overdue_books[username] = {"first_name": user.get_firstname()}
                            overdue_books[username].update({
                                "books": [book.get_title()]
                            })
                        else:
                            overdue_books[username]["books"].append(book.get_title())
        return overdue_books

    def show_overdue_books(self):
        overdue_books = self.overdue_books(list_users)
        for username, details in overdue_books.items():
            print(f"User: {username}")
            print(f"\tName: {details['first_name']}")
            print(f"\tBook(s): {details['books']}")
            print()
        else:
            print("No overdue books found")


if __name__ == "__main__":
    loans = Loans()

    user_ = generate_user()
    list_users = UserList()
    list_users.store_user(user_)
    print()

    book_ = Book()
    loans.borrow_book(user_, book_)

    book_ = Book()
    loans.borrow_book(user_, book_)

    print()

    loans.show_overdue_books()
