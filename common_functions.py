from types import UnionType
from typing import Iterable


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
    if isinstance(seq, ignores):
        return [seq]
    for element in seq:
        if isinstance(element, Iterable) and not isinstance(element, ignores):
            # this is to handle Iterables that directly or indirectly yield themselves
            if element in _parents:
                unpacked.append(element)
            else:
                unpacked.extend(deep_unpack(element, ignores, _parents+(element,)))
        else:
            unpacked.append(element)
    return unpacked


def _table_row(*items: str) -> str:
    """table_row(*items) Generates a row of a Markdown table

    *items: the items of the row"""
    if len(items) < 1:
        raise ValueError('there must be at least one item')
    row: str = '|'.join(items)
    row = '|' + row + '|'
    return row
def table(col: int, *items: str) -> str:
    """table(*items) Generates a Markdown table

    col: the number of columns
    *items: the items in the table"""
    if len(items) % col != 0:
        raise ValueError('the items must fit evenly into the columns')
    rows_num: int = len(items) // col
    if rows_num < 2:
        raise ValueError('there must be at least two rows')
    row1: list = list(items[0:col])
    rows2: list = []
    # calculate number of rows2
    for i in range(rows_num):
        # the range of indexes that correspond to rows2
        rows2.append(_table_row(*items[col * i:col * (i + 1)]), )
    # calculate how to add the -'s
    header_indication: str = '|'
    for i in range(len(row1)):
        header_indication = header_indication + '---|'
    rows2.insert(1, header_indication)
    return '\n'.join(rows2)
