from .connection import Connection
from typing import Dict, List


class MySQL(Connection):

    def __init__(self, /) -> None:
        super().__init__()


    def get_version(self, /) -> Dict[str, str]:
        return self.execute("SELECT version();")[0]


    def show_databases(self, /) -> List[Dict[str, str]]:
        return self.execute("SHOW DATABASES;")
