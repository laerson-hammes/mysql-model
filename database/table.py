from .execute import Execute
# from ..fields.int import IntTypes
# from ..fields.fields import Fields


class Table(Execute):

    def __init__(self, table: str, /) -> None:
        super().__init__()
        self.table = table


    def create(self, /) -> bool:
        pass


    def drop(self, /) -> bool:
        return self.execute(f"DROP TABLE {self.table};")


    def describe(self, /):
        return self.execute(f"DESCRIBE TABLE {self.table};")
