from typing import Iterable
from types import UnionType
def rows(values: list, rows2: int) -> list[list]:
    """Breaks data up into a given number of rows

    values: the data
    rows2: the number of rows"""
    row_len: int = len(values) // rows2
    return_rows: list = []
    for i in range(rows2):
        return_rows.append(values[i * row_len:(i + 1) * row_len])
    return return_rows
def deep_unpack(seq: Iterable[Iterable], ignores: type | UnionType = str, _parents:tuple=()) -> list:
    """Unpacks an Iterable of Iterables into a single Iterable

    seq: the Iterable
    ignores: the types of Iterables to ignore"""
    unpacked: list = []
    for element in seq:
        if isinstance(element, Iterable) and not isinstance(element, ignores):
            # this is to avoid the infinite recursion that occurs because a string contains a string which contains a string, etc.
            if isinstance(element, str) and len(element) == 1:
                unpacked.append(element)
            else:
                unpacked.extend(deep_unpack(element, ignores, _parents))
        else:
            unpacked.append(element)
    return unpacked