from common_functions import *
def test_rows() -> None:
    """test_rows()
    Tests the rows function"""
    assert rows([1, 2], 1) == [[1, 2]]
    assert rows([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert rows([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]
    assert rows([1, 2, 3, 4, 5, 6], 2) == [[1, 2, 3], [4, 5, 6]]
test_rows()