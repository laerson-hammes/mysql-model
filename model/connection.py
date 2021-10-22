import pymysql.cursors
from pymysql.err import OperationalError
from typing import Any, Dict


class ConnectionAttributes(object):
    
    ATTRS: Dict[str, Any] = {
        'host': 'localhost',
        'user': 'root',
        'port': None,
        'password': '',
        'autocommit': True,
        'cursorclass': pymysql.cursors.DictCursor
    }


    def update_atribute(self, **kwargs: Dict[str, Any]) -> None:
        self.ATTRS.update(kwargs)
        print(self.ATTRS)


class Connection(ConnectionAttributes):

    def __init__(self, /) -> None:
        super().__init__()


    def execute(self, query: str, /) -> Any:
        connection = self.connect()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall() or cursor.rowcount or cursor.fetchone()


    def connect(self, /):
        try:
            return pymysql.connect(**self.ATTRS)
        except OperationalError:
            raise OperationalError()
