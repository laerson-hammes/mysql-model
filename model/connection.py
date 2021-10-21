import pymysql.cursors
from pymysql.err import OperationalError
from typing import Any, Dict, Union


class Connection(object):
    
    HOST: str = 'localhost'
    USER: str = 'root'
    PORT: Union[int, None] = None
    PASSWORD: str = ''
    AUTOCOMMIT: bool = True
    CURSORCLASS: type = pymysql.cursors.DictCursor
    
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.__kwargs: Dict[str, Any] = kwargs
        self.connect()
   
    def execute(self, query: str, /) -> None:
        connection = self.connect()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
   
    def connect(self, /):
        try:
            return pymysql.connect(**self.__kwargs)
        except OperationalError:
            raise OperationalError()
