from .connection import ConnectionAttributes
from .execute import Execute
from typing import Dict, List


class Database(Execute, ConnectionAttributes):

    DEFAULT_CHARSET: str = 'utf8'
    DEFAULT_COLLATE: str = 'utf8_general_ci'

    def __init__(self, database: str, /) -> None:
        super().__init__()
        self.database = database


    def create(self, /) -> int:
        query: str = f"""CREATE DATABASE IF NOT EXISTS {self.database}
                        DEFAULT CHARACTER SET {self.DEFAULT_CHARSET}
                        DEFAULT COLLATE {self.DEFAULT_COLLATE};"""
        return self.execute(query)


    def drop(self, /) -> int:
        return self.execute(f"DROP DATABASE {self.database};")


    def use(self, /) -> None:
        self.update_atribute(database=self.database)  # type: ignore


    def show_tables(self, /) -> List[Dict[str, str]]:
        self.use()
        return self.execute("SHOW TABLES;")
