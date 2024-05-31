import sqlite3

from scripts.book import Book
from utils.constants import BASE_DIR
from utils.logger import log


class BooksDB:
    table_name = "books"

    def __init__(self) -> None:
        super().__init__()
        self.conn = sqlite3.connect(BASE_DIR / "db" / "sqlite3.db")
        self.c = self.conn.cursor()
        self.c.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_date DATE NOT NULL,
                publisher TEXT,
                available_copies INTEGER
            )
            """
        )

    def create(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise ValueError("Invalid book object")
        self.c.execute(
            f"""
            INSERT INTO {self.table_name}
            (title, author, publication_date, publisher, available_copies)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                book.title,
                book.author,
                book.publication_date,
                book.publisher,
                book.available_copies,
            ),
        )
        self.conn.commit()
        log(f"Book {book.title} added successfully")

    def read(self, _id: int = 0) -> list[tuple] | str | None:
        try:
            if _id:
                self.c.execute(
                    f"SELECT * FROM {self.table_name} WHERE id = ?",
                    (_id,),
                )
                return self.c.fetchone()
            self.c.execute(f"SELECT * FROM {self.table_name}")
            return self.c.fetchall()
        except Exception as ex:
            log(ex)

    def update(self, _id: int, book: Book) -> None:
        if not isinstance(book, Book):
            raise ValueError("Invalid book object")
        self.c.execute(
            f"""
            UPDATE {self.table_name}
            SET title = ?, author = ?, publication_date = ?, publisher = ?, available_copies = ?
            WHERE id = ?
            """,
            (
                book.title,
                book.author,
                book.publication_date,
                book.publisher,
                book.available_copies,
                _id,
            ),
        )
        self.conn.commit()
        log(f"Book '{book.title}' updated successfully")

    def delete(self, _id: int) -> None:
        self.c.execute(
            f"""
            DELETE FROM {self.table_name} WHERE id = ?
            """,
            (_id,),
        )
        self.conn.commit()
        log(f"Book with id '{_id}' deleted successfully")
