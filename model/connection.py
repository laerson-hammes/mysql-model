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


class Connection(ConnectionAttributes):

    def __init__(self, /) -> None:
        super(ConnectionAttributes, self).__init__()


    def connect(self, /):
        try:
            return pymysql.connect(**self.ATTRS)
        except OperationalError:
            raise OperationalError()
