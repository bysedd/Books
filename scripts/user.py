import re
import textwrap
from datetime import datetime

from email_validator import EmailNotValidError, validate_email

from scripts.base_db import BaseDB
from utils.constants import FORMAT
from utils.logger import log
from utils.utils import alt_title, validate_name


class User:
    def __init__(self):
        self.__name: str = None
        self.__house_number: int = None
        self.__street_name: str = None
        self.__postcode: str = None
        self.__email_address: str = None
        self.__date_of_birth: datetime = None

    @staticmethod
    def create_user():
        try:
            name = input("Enter full name: ")
            date_of_birth = input("Enter date of birth (yyyy-MM-DD): ")
            email_address = input("Enter email address: ")
            house_number = input("Enter house number: ")
            street_name = input("Enter street name: ")
            postcode = input("Enter postcode: ")

            user = User()
            user.name = name
            user.date_of_birth = date_of_birth
            user.email_address = email_address if email_address else None
            user.house_number = house_number if house_number else None
            user.street_name = street_name if street_name else None
            user.postcode = postcode if postcode else None
            return user
        except ValueError:
            print("Invalid input. Please try again.")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        validate_name(name)
        self.__name = alt_title(name)

    @property
    def house_number(self) -> int:
        return self.__house_number

    @house_number.setter
    def house_number(self, house_number: int) -> None:
        if house_number is None:
            return
        if not isinstance(house_number, int):
            raise TypeError("House number must be an integer")
        if house_number <= 0:
            raise ValueError("House number must be greater than 0")
        self.__house_number = int(house_number)

    @property
    def street_name(self) -> str:
        return self.__street_name

    @street_name.setter
    def street_name(self, street_name: str) -> None:
        if street_name is None:
            return
        validate_name(street_name)
        self.__street_name = street_name.strip()

    @property
    def postcode(self) -> str:
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode: str) -> None:
        if postcode is None:
            return
        postcode = re.sub(r"\s+", "", postcode)
        if len(postcode) < 5:
            raise ValueError("Postcode should be at least 5 characters long")
        if not postcode.isdigit():
            raise ValueError("Postcode should contain only numbers")
        self.__postcode = postcode

    @property
    def email_address(self) -> str:
        return self.__email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        if email_address is None:
            return
        try:
            valid = validate_email(email_address)
            self.__email_address = valid.email
        except EmailNotValidError as e:
            log(str(e))

    @property
    def date_of_birth(self) -> datetime | str:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str) -> None:
        try:
            datetime.strptime(date_of_birth, FORMAT)
        except ValueError:
            raise ValueError(f"Date of birth should be in the format ({FORMAT})")
        self.__date_of_birth = date_of_birth

    def __str__(self):
        return textwrap.dedent(
            f"""\
            Name: {self.firstname}
            Email address: {self.email_address}
            Date of birth: {self.date_of_birth}
            House number: {self.house_number}
            Street name: {self.street_name}
            Postcode: {self.postcode}
            """
        )


class UsersDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.c.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_birth DATE NOT NULL,
                email TEXT,
                house_number INTEGER,
                street_name TEXT,
                postcode TEXT
            )
            """
        )

    @property
    def table_name(self) -> str:
        return "users"

    def create(self, obj: User):
        try:
            self.c.execute(
                f"""
                INSERT INTO {self.table_name} (name, email, date_of_birth, house_number, street_name, postcode)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    obj.name,
                    obj.email_address,
                    obj.date_of_birth,
                    obj.house_number,
                    obj.street_name,
                    obj.postcode,
                ),
            )
            self.conn.commit()
            log(f"User '{obj.name}' stored successfully")
        except Exception as ex:
            raise Exception(f"Failed to store user due to {ex}")

    def update(self, primary_key: int, obj: User) -> None:
        date_of_birth = obj.date_of_birth
        if not isinstance(obj.date_of_birth, datetime):
            date_of_birth = datetime.strptime(obj.date_of_birth, FORMAT)
        self.c.execute(
            f"""
            UPDATE {self.table_name}
            SET name = ?, email = ?, date_of_birth = ?, house_number = ?, street_name = ?, postcode = ?
            WHERE id = ?
            """,
            (
                obj.name,
                obj.email_address,
                date_of_birth,
                obj.house_number,
                obj.street_name,
                obj.postcode,
                primary_key,
            ),
        )
        log(f"User '{obj.name}' updated successfully")
