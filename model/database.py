from connection import Connection
from typing import Any, Dict, Union
import pymysql.cursors


class Database(Connection):

    DEFAULT_CHARSET: str = 'utf8'
    DEFAULT_COLLATE: str = 'utf8_general_ci'
    DATABASE_NAME: Union[str, None] = None
   
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        super().__init__(**kwargs)

    def create(self, database: str) -> None:
        self.DATABASE_NAME = database
        query: str = f"""CREATE DATABASE IF NOT EXISTS {database}
                        DEFAULT CHARACTER SET {self.DEFAULT_CHARSET}
                        DEFAULT COLLATE {self.DEFAULT_COLLATE};"""
        self.execute(query)

    def drop(self) -> None:
        if self.DATABASE_NAME:
            self.execute(f"DROP DATABASE {self.DATABASE_NAME};")
      
    def use(self) -> None:
        if self.DATABASE_NAME:
            self.execute(f"USE {self.DATABASE_NAME};")
      

if __name__ == "__main__":
    db: Database = Database(host='localhost', user='root', password='', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    print(db.execute("SHOW DATABASES;")[0]['Database'])
