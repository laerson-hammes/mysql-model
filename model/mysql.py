from .execute import Execute
from typing import Dict, List


class MySQL(Execute):

    def __init__(self, /) -> None:
        super(Execute, self).__init__()


    def get_version(self, /) -> Dict[str, str]:
        return self.execute("SELECT version();")[0]


    def show_databases(self, /) -> List[Dict[str, str]]:
        return self.execute("SHOW DATABASES;")


    def get_variables(self, /) -> List[Dict[str, str]]:
        return self.execute("SHOW VARIABLES;")
    

    def get_hostname(self, /) -> List[Dict[str, str]]:
        return self.execute("SHOW VARIABLES WHERE Variable_name = 'hostname';")


    def get_port(self, /) -> List[Dict[str, str]]:
        return self.execute("SHOW VARIABLES WHERE Variable_name = 'port';")


    def get_specific_variable(self, variable: str, /) -> List[Dict[str, str]]:
        return self.execute(f"SHOW VARIABLES WHERE Variable_name = '{variable}';")
