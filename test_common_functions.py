from common_functions import *
def test_function_points()->None:
    """test_function_points() Tests the function_points function"""
    assert len(function_points(lambda x: x,0,10))==101
    assert function_points(lambda x: x,0,100)[50][1]==50
    for points in function_points(lambda x: x,0,100, 10):
        assert points[0]==points[1]
    assert len(function_points(lambda x: x,0,100,10))==10
    for points in function_points(lambda x: x**2,55,234,17):
        assert points[0]**2==points[1]
    assert function_points(lambda x: x**2,1,10,10)[5][1]==25
def test_function_lines()->None:
    """test_function_lines() Tests the function_lines function"""
    assert len(function_lines(lambda x: x,0,10))==100
    assert function_lines(lambda x: x,0,10,10)[0][0]==sqrt(2)
    assert function_lines(lambda x: x, 0, 10, 15)[0][1] == 45
    for line in function_lines(lambda x: x,0,10,10):
        assert line[0]==sqrt(2)
        assert line[1]==45
    assert len(function_lines(lambda x: x, 15,67,45))==45
    assert function_lines(lambda x: x**2, 0, 10, 10)[0][0] == sqrt(2)
    assert function_lines(lambda x: x**2, 0, 10, 10)[0][1] == 45
def test_sym_dict()->None:
    """test_sym_dict() Tests the sym_dict function"""
    assert sym_dict({})=={}
    assert sym_dict({1:2, 3:4})=={1:2,3:4,2:1,4:3}
    assert sym_dict({1:2,3:4,2:1})=={1:2,2:1,3:4,4:3}
def test_same_letter()->None:
    """test_same_letter() Tests the same_letter function"""
    assert same_letter('','')
    assert same_letter('#','#')
    assert same_letter('#','a') is False
    assert same_letter('a','#') is False
    assert same_letter('a','A')
    assert same_letter('a','B') is False
def test_same_letters()->None:
    """test_same_letters() Tests the same_letters function"""
    assert same_letters('a','ab') is False
    assert same_letters('$%^','$%^')
    assert same_letters('!@#','#@!') is False
    assert same_letters('abc','ABC')
    assert same_letters('abc','CBA') is False
    assert same_letters('abc','cba') is False
    assert same_letters('a$%B','A$%b')
test_function_points()
test_function_lines()
test_sym_dict()
test_same_letter()
test_same_letters()