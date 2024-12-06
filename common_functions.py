from collections.abc import Iterable, Callable, Sequence, Mapping
from math import sqrt, atan, pi
from types import UnionType

Number = int | float

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


def _function_points(f: Callable[[Number], Number], start: Number, end: Number, n: int = 101) -> tuple[
    tuple[Number, Number]]:
    """Returns a series of ordered pairs from a given function

    f: a python function that takes one numerical input and produces one numerical output
    start: the input to start the computation at
    end: the input to end the computation at
    n: the number of points to compute"""
    step: Number = (end - start) / (n - 1)
    points: tuple = ()
    for i in range(n):
        x: Number = i * step
        y: Number = f(x)
        points = points + ((x, y),)
    return points


def function_lines(f: Callable[[Number], Number], start: Number, end: Number, n: int = 100) -> tuple[
    tuple[Number, Number]]:
    """Returns a series of lines (length, heading) approximating a function

    f: a python function that takes one numerical input and produces one numerical output
    start: the input to start the computation at
    end: the input to end the computation at
    n: the number of lines to compute"""
    points: tuple = _function_points(f, start, end, n + 1)
    lines: tuple = ()
    # iterates through every element in points except the last
    for index, point in enumerate(points[0:-1]):
        x1: Number = point[0]
        y1: Number = point[1]
        x2: Number = points[index + 1][0]
        y2: Number = points[index + 1][1]
        length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        slope: Number = (y2 - y1) / (x2 - x1)
        radian_heading = atan(slope)
        heading = radian_heading * 180 / pi
        lines = lines + ((length, heading),)
    return lines


def fetch(seq: Sequence | Mapping, indexes: list) -> list:
    """Retrieves the requested indexes from a sequence, this primarily for retrieving multiple data points from a
    complex data structure

    seq: the sequence to retrieve from
    indexes: a list of 'pathways' to the requested data, values that are simply indexes or keys will be simply
    retrieved. If the value is a list the first value in the list is taken to be the index to a subsequence in seq
    and the other values are taken to be the indexes of values desired from that subsequence (these can also be lists
    in order to retrieve from sub-subsequences)"""
    items: list = []
    for index in indexes:
        if isinstance(index, list):
            items.extend(fetch(seq[index[0]], index[1:]))
        else:
            items.append(seq[index])
    return items
