import re
from datetime import datetime

from email_validator import validate_email, EmailNotValidError
from faker import Faker

from utils.logger import log


class Users:
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

        Checks whether the new date of birth follows the format 'MM-DD-YYYY'.
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


def generate_user(*, first_name: str = None) -> Users:
    faker = Faker()

    fake_email = faker.email()
    username, _domain = fake_email.split("@")
    fake_gmail = username + "@gmail.com"

    return Users(
        faker.user_name(),
        first_name or faker.first_name(),
        faker.last_name(),
        faker.building_number(),
        faker.street_name(),
        faker.postcode(),
        fake_gmail,
        faker.date_of_birth(maximum_age=90),
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
