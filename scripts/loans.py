from datetime import datetime, timedelta


class Loans:
    def __init__(self):
        self.loan_records = {}

    def borrow_book(self, user, book):
        if user.get_username() in self.loan_records:
            self.loan_records[user.get_username()].append(book)
        else:
            self.loan_records[user.get_username()] = [book]

    def return_book(self, user, book):
        if (
            user.get_username() in self.loan_records
            and book in self.loan_records[user.get_username()]
        ):
            self.loan_records[user.get_username()].remove(book)

    def count_borrowed_books(self, user):
        if user.get_username() in self.loan_records:
            return len(self.loan_records[user.get_username()])
        else:
            return 0

    def overdue_books(self, users):
        today = datetime.now()
        overdue_books = {}
        for username, borrowed_books in self.loan_records.items():
            for book in borrowed_books:
                due_date = datetime.strptime(
                    book.get_publication_date(), "%Y-%m-%d"
                ) + timedelta(days=30)
                if due_date < today:
                    user = users.user_collection.get(username)
                    if user:
                        if username not in overdue_books:
                            overdue_books[username] = user.get_firstname()
        return overdue_books
