from common_functions import *
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
test_rows()
test_deep_unpack()