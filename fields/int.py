from collections.abc import Callable


class IntTypes(object):

    """
    Storage (Bytes): 1
    Minimum Value Signed: -128
    Minimum Value Unsigned: 0
    Maximum Value Signed: 127
    Maximum Value Unsigned: 255
    """
    TINYINT = int

    """
    Storage (Bytes): 2
    Minimum Value Signed: -32768
    Minimum Value Unsigned: 0
    Maximum Value Signed: 32767
    Maximum Value Unsigned: 65535
    """
    SMALLINT = int

    """
    Storage (Bytes): 3
    Minimum Value Signed: -8388608
    Minimum Value Unsigned: 0
    Maximum Value Signed: 8388607
    Maximum Value Unsigned: 16777215
    """
    MEDIUMINT = int

    """
    Storage (Bytes): 4
    Minimum Value Signed: -2147483648
    Minimum Value Unsigned: 0
    Maximum Value Signed: 2147483647
    Maximum Value Unsigned: 4294967295
    """
    INTEGER = int

    """
    Storage (Bytes): 8
    Minimum Value Signed: -2 ** 63
    Minimum Value Unsigned: 0
    Maximum Value Signed: 2 ** 63 - 1
    Maximum Value Unsigned: 2 ** 64 - 1
    """
    BIGINT = int


class VerifyIntTypes(object):
    def __init__(self, /) -> None:
        pass


    def tinyint(self, value, unsigned, /) -> bool:
        if unsigned:
            return value >= 0 and value <= 255
        return value >= -128 and value <= 127
    

    def smallint(self, value, unsigned, /) -> bool:
        if unsigned:
            return value >= 0 and value <= 65535
        return value >= -32768 and value <= 32767


    def mediumint(self, value, unsigned, /) -> bool:
        if unsigned:
            return value >= 0 and value <= 16777215
        return value >= -8388608 and value <= 8388607

 
    def integer(self, value, unsigned, /) -> bool:
        if unsigned:
            return value >= 0 and value <= 4294967295
        return value >= -2147483648 and value <= 2147483647


    def bigint(self, value, unsigned, /) -> bool:
        if unsigned:
            return value >= 0 and value <= 18446744073709551615
        return value >= -9223372036854775808 and value <= 9223372036854775807


    def verify_type(self, type: Callable[[int, bool], bool], *, value: int, unsigned: bool = True) -> bool:
        return type(value, unsigned)


if __name__ == "__main__":
    v: VerifyIntTypes = VerifyIntTypes()
    print(v.verify_type(v.tinyint, value=127, unsigned=True))
