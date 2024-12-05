from io import StringIO

from common_functions import *
from common_functions import _table_row


def inner(outer:Iterable)->Iterable:
    """This generator tests how deep_unpack handles Iterables that indirectly contain references to themselves

    outer2: should be a generator that yields inner(outer) thus creating a circular reference"""
    yield outer
class Outer:
    """This generator tests how deep_unpack handles Iterables that indirectly contain references to themselves"""
    def __init__(self)->None:
        pass
    def __iter__(self):
        yield inner(self)
def test_rows() -> None:
    """test_rows()
    Tests the rows function"""
    assert rows([1, 2], 1) == [[1, 2]]
    assert rows([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert rows([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]
    assert rows([1, 2, 3, 4, 5, 6], 2) == [[1, 2, 3], [4, 5, 6]]
def test_deep_unpack() -> None:
    """Tests the deep_unpack function"""
    assert deep_unpack([[None, 'abc', 1.2], [True, 3], ['ghf']]) == [None, 'abc', 1.2, True, 3, 'ghf']
    assert deep_unpack([[['abc', None], [], 2.34], [[], [True, 3]]]) == ['abc', None, 2.34, True, 3]
    assert deep_unpack([[(1, 2, 3), ('abc', 'efg')], ['abc']], tuple) == [(1, 2, 3), ('abc', 'efg'), 'a', 'b', 'c']
    assert deep_unpack([[(1, 2, 3), ('abc', 'efg')], ['abc']], tuple | str) == [(1, 2, 3), ('abc', 'efg'), 'abc']
    assert deep_unpack('abc')==['abc']
    circular:Outer = Outer()
    assert deep_unpack(circular)==[circular]


def test_table_row() -> None:
    """Tests the _table_row function"""
    try:
        assert _table_row()
        assert False
    except ValueError:
        pass
    assert _table_row('a') == '|a|'
    assert _table_row('a', 'b') == '|a|b|'
    assert _table_row('a', 'b', 'c') == '|a|b|c|'
def test_table() -> None:
    """Tests the table function"""
    with StringIO() as test:
        test.write(table(2, 'a', 'b', 'c', 'd'))
        assert test.getvalue() == '|a|b|\n|---|---|\n|c|d|'
    with StringIO() as test:
        test.write(table(3, 'aaa', 'bjk', 'as', 'asd', 'asd', 're'))
        assert test.getvalue() == '|aaa|bjk|as|\n|---|---|---|\n|asd|asd|re|'
    with StringIO() as test:
        test.write(table(2, 'a', 'b', 'c', 'd', 'e', 'f'))
        assert test.getvalue() == '|a|b|\n|---|---|\n|c|d|\n|e|f|'
test_rows()
test_deep_unpack()
test_table_row()
test_table()