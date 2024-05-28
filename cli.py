import cmd
import os

from scripts.book import Book
from scripts.books_db import BooksDB
from utils.constants import ASCII_ART
from utils.utils import title_msg


class LibraryCMD(cmd.Cmd):
    """
    Command processor for library management.
    """

    intro = ASCII_ART
    intro += (
        "\nWelcome to the library system. Type 'help' or '?' to list the commands.\n"
    )

    def __init__(self):
        super().__init__()
        self.books_db = BooksDB()

    def do_create(self, line):
        """
        Create a book
        usage: create
        """
        print(title_msg("Creating book"))
        book = Book.create_book()
        if book:
            self.books_db.create(book)

    def do_read(self, line):
        """
        Read a book or user
        usage: read
        """
        print(title_msg("Reading"))
        try:
            _id = int(input("Enter id: "))
        except ValueError:
            print("Invalid id.")
            return

        book = self.books_db.read(_id)
        if book:
            print(title_msg("Book information"))
            print(book)
        else:
            print("Book not found.")

    def do_update(self, line):
        """
        Update a book or user
        usage: update
        """
        print(title_msg("Updating book"))
        try:
            _id = int(input("Enter id: "))
        except ValueError:
            print("Invalid id.")
            return

        book = self.books_db.read(_id)
        if book:
            print(title_msg("New book information"))
            new_book = Book.create_book()
            if new_book:
                self.books_db.update(_id, new_book)
        else:
            print("Book not found.")

    def do_delete(self, line):
        """
        Delete a book or user
        usage: delete
        """
        print(title_msg("Deleting book"))
        try:
            _id = int(input("Enter id: "))
        except ValueError:
            print("Invalid id.")
            return

        book = self.books_db.read(_id)
        if book:
            self.books_db.delete(_id)
        else:
            print("Book not found.")

    def do_help(self, arg):
        """
        Display help information.
        """
        commands = {
            "create": "Create a new book or user",
            "read": "Read a book or user",
            "update": "Update a book or user",
            "delete": "Delete a book or user",
            "exit": "Exit the program.",
            "clear": "Clear the terminal.",
        }

        if arg in commands:
            print(f"{arg}: {commands[arg]}")
        else:
            for cmd_, desc in commands.items():
                print(f"{cmd_}: {desc}")

    @staticmethod
    def do_exit(line):
        """
        Stop the command loop
        usage: exit
        """
        raise KeyboardInterrupt

    @staticmethod
    def do_clear(line):
        """
        Clear the terminal
        usage: clear
        """
        os.system("cls" if os.name == "nt" else "clear")


def main():
    try:
        LibraryCMD().cmdloop()
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
