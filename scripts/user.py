import re
from datetime import datetime
from typing import Dict

from django.utils.text import slugify
from email_validator import validate_email, EmailNotValidError
from faker import Faker

from utils.logger import log


class User:
    """
    User class for storing user personal information.
    """

    def __init__(
        self,
        username: str,
        firstname: str,
        surname: str,
        house_number: int,
        street_name: str,
        postcode: str,
        email_address: str,
        date_of_birth: datetime,
    ):
        """
        Initializes the User object with personal details.

        :param username: User's unique username
        :param firstname: User's first name
        :param surname: User's last name
        :param house_number: User's house number
        :param street_name: User's street name
        :param postcode: User's zip code
        :param email_address: User's email address
        :param date_of_birth: User's birthday.
        """
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email_address = email_address
        self.date_of_birth = date_of_birth

    def get_username(self):
        """Returns the user's username."""
        return self.username

    def get_firstname(self):
        """Returns the user's first name."""
        return self.firstname

    def get_surname(self):
        """Returns the user's surname."""
        return self.surname

    def get_house_number(self):
        """Returns the user's house number."""
        return self.house_number

    def get_street_name(self):
        """Returns the user's street name."""
        return self.street_name

    def get_postcode(self):
        """Returns the user's zip code."""
        return self.postcode

    def get_email_address(self):
        """Returns the user's email address."""
        return self.email_address

    def get_date_of_birth(self):
        """Returns the user's date of birth."""
        return self.date_of_birth

    def set_firstname(self, new_firstname: str):
        """Updates the user's first name."""
        new_firstname = new_firstname.strip()
        if self.__validate_name(new_firstname):
            self.firstname = new_firstname

    def set_surname(self, new_surname: str):
        """Updates the user's surname."""
        new_surname = new_surname.strip()
        if self.__validate_name(new_surname):
            self.surname = new_surname

    def set_housenumber(self, new_house_number: int):
        """Updates the user's house number."""
        try:
            self.house_number = int(new_house_number)
        except ValueError:
            log("House number should be an integer")

    def set_streetname(self, new_street_name: str):
        """Updates the user's street name."""
        new_street_name = new_street_name.strip()
        if self.__validate_name(new_street_name):
            self.street_name = new_street_name

    def set_postcode(self, new_postcode: str):
        """Updates the user's zip code."""
        new_postcode = new_postcode.strip()
        if len(new_postcode) < 5:
            log("Postcode should be at least 5 characters long")
        elif not bool(re.fullmatch("[A-Za-z0-9 ]+", new_postcode)):
            log("Postcode should only contain letters, numbers, and spaces")
        else:
            self.postcode = new_postcode

    def set_email_address(self, new_email: str):
        """
        Updates the user's email address.

        It checks whether the new email address has a valid format.
        """
        try:
            valid = validate_email(new_email)
            self.email_address = valid.email
        except EmailNotValidError as e:
            log(str(e))

    def set_date_of_birth(self, new_dob: str):
        """
        Updates the user's date of birth.

        Checks whether the new date of birth follows the format 'MM-DD-yyyy'.
        """
        try:
            datetime.strptime(new_dob, "%m-%d-%Y")
        except ValueError:
            log("Date of birth should be in the format 'MM-DD-YYYY'")

        self.date_of_birth = new_dob

    @staticmethod
    def __validate_name(name: str):
        if not isinstance(name, str):
            log("Name should be a string")
        elif len(name) < 2:
            log("Name should be at least 2 characters long")
        elif not bool(re.fullmatch("[A-Za-z ]+", name)):
            log("Name should only contain letters and spaces")
        else:
            return True
        return False

    def __str__(self):
        return f"""Username: {self.username}
First name: {self.firstname}
Surname: {self.surname}
House number: {self.house_number}
Street name: {self.street_name}
Postcode: {self.postcode}
Email address: {self.email_address}
Date of birth: {self.date_of_birth}"""

    def modify(self):
        print(f"Modifying user '{self.get_username()}'")
        new_firstname = input(
            "Enter new first name ('Enter' to leave unchanged): "
        ).strip()
        new_surname = input("Enter new surname ('Enter' to leave unchanged): ").strip()
        new_house_number = input(
            "Enter new house number ('Enter' to leave unchanged): "
        ).strip()
        new_street_name = input(
            "Enter new street name ('Enter' to leave unchanged): "
        ).strip()
        new_postcode = input(
            "Enter new postal code ('Enter' to leave unchanged): "
        ).strip()

        if new_firstname:
            self.set_firstname(new_firstname)
        if new_surname:
            self.set_surname(new_surname)
        if new_house_number:
            self.set_housenumber(int(new_house_number))
        if new_street_name:
            self.set_streetname(new_street_name)
        if new_postcode:
            self.set_postcode(new_postcode)


class UserList:
    """
    This class provides capabilities for storing, searching for, and deleting User instances.
    """

    def __init__(self):
        """
        This constructor creates a new dictionary collection for User instances.
        """
        self.user_collection: Dict[str, User] = {}

    def store_user(self, user_: User):
        """
        This method stores a User instance in the collection.

        :param user_: The User instance to store.
        """
        try:
            if user_.username in self.user_collection:
                log(f"User '{user_.username}' already stored")
                return
            self.user_collection[user_.username] = user_
            log(f"User '{user_.username}' stored successfully")
        except Exception as ex:
            log(f"Failed to store user '{user_.username}' due to {ex}")

    def remove_user(self, first_name: str):
        """
        This method removes a user by their first name.

        If many users with the same first name exist, it informs the program users.

        :param first_name: The first name of the user to remove.
        """
        try:
            matching_users = [
                user_
                for user_ in self.user_collection.values()
                if user_.firstname == first_name
            ]

            if len(matching_users) > 1:
                log(
                    f"Warning: More than one user with the first name '{first_name}' exists."
                )
                usernames = ", ".join([user_.username for user_ in matching_users])
                log(f"Users with first name '{first_name}': {usernames}")
                username = input("Enter the username of the user you want to remove: ")

                if (
                    username in self.user_collection
                    and self.user_collection[username].firstname == first_name
                ):
                    del self.user_collection[username]
                    log(f"User '{username}' removed successfully")
                else:
                    log(
                        f"No user with username '{username}' and first name '{first_name}'"
                    )

            elif len(matching_users) == 1:
                for username, user_ in self.user_collection.items():
                    if user_ == matching_users[0]:
                        del self.user_collection[username]
                        log(f"User '{username}' removed successfully")
                        break

            else:
                log(f"No user with first name '{first_name}'")

        except Exception as ex:
            log(f"Failed to remove {first_name}'s user due to {ex}")

    def count_users(self) -> int:
        """
        This method returns the count of users in the system.

        This should be based on the number of user objects in the user collection.

        :return: Total count of users
        """
        return len(self.user_collection)

    def get_user(self, username: str) -> User:
        """
        This method returns a user's detail by the username.

        :param username: The username of the user.
        :return: The User instance.
        """
        try:
            return self.user_collection[username]
        except Exception as ex:
            log(f"An error occurred: {ex}")

    def __repr__(self):
        return f"{type(self).__name__}({self.__dict__!r})"


def generate_user(first_name: str = None, last_name: str = None) -> User:
    faker = Faker()

    unique_id = faker.random_number(digits=4, fix_len=True)
    first_name = first_name or faker.first_name()
    username_slug = slugify(first_name)
    unique_username = f"{username_slug}-{unique_id}"

    last_name = last_name or faker.last_name()

    fake_gmail = f"{first_name}.{last_name}{unique_id}@gmail.com".lower()

    return User(
        unique_username,
        first_name,
        last_name,
        faker.building_number(),
        faker.street_name(),
        faker.postcode(),
        fake_gmail,
        faker.date_of_birth(maximum_age=115),
    )


if __name__ == "__main__":
    user = generate_user()

    print(user)
    print("-=" * 20)

    user.set_firstname("John")
    user.set_surname("Doe")
    user.set_email_address(
        "this is not a valid email address"
    )  # should not update the email address
    user.set_email_address("john.doe@gmail.com")
    user.set_date_of_birth("28-01-2000")  # should not update the date of birth
    user.set_date_of_birth("01-28-2000")

    print(user)

    user_list = UserList()

    user1 = generate_user(first_name="Patrick")
    user2 = generate_user(first_name="Patrick")

    user_list.store_user(user1)
    user_list.store_user(user2)
    print()

    print(user_list.get_user(user1.username))
    print()
    print(user_list.get_user(user2.username))
    print()

    user_list.remove_user("Patrick")
    print()

    print(f"Total users: {user_list.count_users()}")
