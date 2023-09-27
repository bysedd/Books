import cmd
import os

from scripts.book import BookList, Book
from scripts.user import UserList, User, generate_user


class LibraryCMD(cmd.Cmd):
    """
    Command processor for library management.
    """

    intro = """
 _       _________ ______   _______  _______  _______          
( \      \__   __/(  ___ \ (  ____ )(  ___  )(  ____ )|\     /|
| (         ) (   | (   ) )| (    )|| (   ) || (    )|( \   / )
| |         | |   | (__/ / | (____)|| (___) || (____)| \ (_) / 
| |         | |   |  __ (  |     __)|  ___  ||     __)  \   /  
| |         | |   | (  \ \ | (\ (   | (   ) || (\ (      ) (   
| (____/\___) (___| )___) )| ) \ \__| )   ( || ) \ \__   | |   
(_______/\_______/|/ \___/ |/   \__/|/     \||/   \__/   \_/   
    """
    intro += (
        "\nWelcome to the library system. Type 'help' or '?' to list the commands.\n"
    )

    def __init__(self):
        super().__init__()
        self.book_list = BookList()
        self.user_list = UserList()

    def do_add_book(self, line):
        """
        Add a book
        usage: add_book
        """
        book = Book()
        print("Adding a new book")
        try:
            title = input("Enter book title: ")
            book.set_title(title)
            author = input("Enter book author: ")
            book.set_author(author)
            year = int(input("Enter book publication year: "))
            book.set_year(year)
            publisher = input("Enter book publisher: ")
            book.set_publisher(publisher)
            available_copies = int(input("Enter number of available copies: "))
            book.set_available_copies(available_copies)
            self.book_list.store_book(book)
        except ValueError:
            print("Invalid input. Please try again.")

    def do_add_user(self, line):
        """
        Add a user
        usage: add_user
        """
        print("Adding a new user")
        try:
            firstname = input("Enter first name: ")
            surname = input("Enter surname: ")
            house_number = int(input("Enter house number: "))
            street_name = input("Enter street name: ")
            postcode = input("Enter postcode: ")
        except ValueError:
            print("Invalid input. Please try again.")
            return

        generated_user = generate_user(firstname)
        user = User(
            username=generated_user.get_username(),
            firstname=firstname,
            surname=surname,
            house_number=house_number,
            street_name=street_name,
            postcode=postcode,
            date_of_birth=generated_user.get_date_of_birth(),
            email_address=generated_user.get_email_address(),
        )
        self.user_list.store_user(user)

    def do_mod_book(self, line):
        """
        Change a book
        usage: mod_book
        """
        try:
            id_ = int(input("Enter book id to modify: "))
        except ValueError:
            print("Invalid book id.")
            return

        book = self.book_list.book_collection.get(id_)
        if book:
            print(f"Modifying Book '{book.get_title()}'")
            new_title = input("Enter new title ('Enter' to leave unchanged): ")
            if new_title:
                book.set_title(new_title)
        else:
            print(f"No book with id {id_} found.")

    def do_mod_user(self, line):
        """
        Change a user
        usage: mod_user
        """
        username = input("Enter username: ")
        user = self.user_list.get_user(username)
        if user:
            user.modify()
        else:
            print(f"No user with username {username} found.")

    def do_view_book(self, line):
        """
        View a book
        usage: view_book <id>
        """
        try:
            id_ = int(input("Enter book id to view: "))
        except ValueError:
            print("Invalid book id.")
            return

        book = self.book_list.book_collection.get(id_)
        if book:
            print(book)
        else:
            print(f"No book with id {id_} found.")

    def do_view_user(self, line):
        """
        View a user
        usage: view_user <username>
        """
        username = input("Enter the username: ")
        user = self.user_list.get_user(username)
        if user:
            print(user)
        else:
            print(f"No user with username {username} found.")

    def do_help(self, arg):
        """
        Display help information.
        """
        commands = {
            "add_book": "Add a new book.",
            "add_user": "Add a new user.",
            "mod_book": "Modify an existing book.",
            "mod_user": "Modify an existing user.",
            "view_book": "View information of a book. Example: view_book <id>",
            "view_user": "View information of a user. Example: view_user <username>",
            "exit": "Exit the program.",
            "clear": "Clear the terminal.",
        }

        if arg in commands:
            print(f"{arg}: {commands[arg]}")
        else:
            print("Available commands:")
            for cmd_, desc in commands.items():
                print(f"{cmd_}: {desc}")

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    @staticmethod
    def do_exit(line):
        """
        Stop the command loop
        usage: exit
        """
        return True

    @staticmethod
    def do_clear(line):
        """
        Clear the terminal
        usage: clear
        """
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    try:
        LibraryCMD().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
