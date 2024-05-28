import cmd
import os

from scripts.book import Book, BooksDB
from scripts.user import User, UsersDB
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
        self.users_db = UsersDB()

    def do_create(self, line):
        """
        Create a book or user
        usage: create
        """
        print(title_msg("Creating..."))
        option = input("Enter 'book' or 'user': ").strip().lower()
        match option:
            case "book":
                book = Book.create_book()
                if book:
                    self.books_db.create(obj=book)
            case "user":
                user = User.create_user()
                if user:
                    self.users_db.create(obj=user)
            case _:
                print("Invalid option.")

    def do_read(self, line):
        """
        Read a book or user
        usage: read
        """
        print(title_msg("Reading..."))
        option = input("Enter 'book' or 'user': ").strip().lower()
        try:
            _id = int(input("Enter id: "))
        except ValueError:
            print("Invalid id.")
            return

        match option:
            case "book":
                book = self.books_db.read(primary_key=_id)
                if book:
                    print(title_msg("Book information"))
                    print(book)
                else:
                    print("Book not found.")
            case "user":
                user = self.users_db.read(primary_key=_id)
                if user:
                    print(title_msg("User information"))
                    print(user)
                else:
                    print("User not found.")
            case _:
                print("Invalid option.")

    def do_update(self, line):
        """
        Update a book or user
        usage: update
        """
        print(title_msg("Updating..."))
        option = input("Enter 'book' or 'user': ").strip().lower()
        try:
            _id = int(input("Enter id: "))
        except ValueError:
            print("Invalid id.")
            return

        match option:
            case "book":
                book = self.books_db.read(primary_key=_id)
                if book:
                    print("Enter new book details:")
                    new_book = Book.create_book()
                    if new_book:
                        self.books_db.update(primary_key=_id, obj=new_book)
                else:
                    print("Book not found.")
            case "user":
                user = self.users_db.read(primary_key=_id)
                if user:
                    print("Enter new user details:")
                    new_user = User.create_user()
                    if new_user:
                        self.users_db.update(primary_key=_id, obj=new_user)
                else:
                    print("User not found.")
            case _:
                print("Invalid option.")

    def do_delete(self, line):
        """
        Delete a book or user
        usage: delete
        """
        print(title_msg("Deleting..."))
        option = input("Enter 'book' or 'user': ").strip().lower()
        try:
            _id = int(input("Enter id: "))
        except ValueError:
            print("Invalid id.")
            return

        match option:
            case "book":
                book = self.books_db.read(primary_key=_id)
                if book:
                    self.books_db.delete(primary_key=_id)
                    print("Book deleted successfully.")
                else:
                    print("Book not found.")
            case "user":
                user = self.users_db.read(primary_key=_id)
                if user:
                    self.users_db.delete(primary_key=_id)
                    print("User deleted successfully.")
                else:
                    print("User not found.")
            case _:
                print("Invalid option.")

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
            print("Available commands:")
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
