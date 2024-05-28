import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime

from utils.constants import ALLOWED_FIELDS, BASE_DIR, FORMAT
from utils.logger import log


class BaseDB(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.conn = sqlite3.connect(BASE_DIR / "db" / "sqlite3.db")
        self.c = self.conn.cursor()

    @classmethod
    def __verify_fields(cls, obj):
        for key, value in obj.__dict__.items():
            if key not in ALLOWED_FIELDS:
                raise ValueError(f"{key} is not a valid field")
            if isinstance(value, datetime):
                try:
                    return datetime.strftime(value, FORMAT)
                except ValueError as ex:
                    log(ex)

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    @abstractmethod
    def create(self, obj) -> None:
        self.__verify_fields(obj)

    def read(self, primary_key, column="id") -> list[tuple] | str | None:
        try:
            if primary_key:
                self.c.execute(
                    f"SELECT * FROM {self.table_name} WHERE {column} = ?",
                    (primary_key,),
                )
                return self.c.fetchone()
            self.c.execute(f"SELECT * FROM {self.table_name}")
            return self.c.fetchall()
        except Exception as ex:
            log(ex)

    @abstractmethod
    def update(self, primary_key, obj) -> None:
        self.__verify_fields(obj)

    def delete(self, primary_key, column="id") -> None:
        self.c.execute(
            f"""
            DELETE FROM {self.TABLE_NAME} WHERE {column} = ?
            """,
            (primary_key,),
        )
        self.conn.commit()
