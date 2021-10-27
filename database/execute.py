from .connection import Connection
from typing import Any


class Execute(Connection):

    def __init__(self, /) -> None:
        super(Execute, self).__init__()


    def execute(self, query: str, /) -> Any:
        connection = self.connect()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                # print(cursor.describe)
                return cursor.fetchall() or cursor.rowcount or cursor.fetchone()
