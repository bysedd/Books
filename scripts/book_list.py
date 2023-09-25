class BookList:
    def __init__(self):
        self.book_collection = {}

    def store_book(self, book):
        self.book_collection[book.book_id] = book

    def search_book(self, key, value):
        found_books = []
        for book in self.book_collection.values():
            if getattr(book, key) == value:
                found_books.append(book)
        return found_books

    def remove_book(self, title):
        for book_id, book in list(self.book_collection.items()):
            if book.title == title:
                del self.book_collection[book_id]

    def total_books(self):
        return len(self.book_collection)
