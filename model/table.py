from .connection import Connection


class Table(Connection):
    def __init__(self, table: str, /) -> None:
        super().__init__()
        self.table = table
        
    
    def create(self, /) -> bool:
        pass
    
    
    def drop(self, /) -> bool:
        pass