from math import sqrt,atan,pi
from random import randint
Number = int | float
def function_points(f,start:Number,end:Number,n:int=101)->tuple[tuple[Number,Number],...]:
    """function_points(f, start, end, n=101) Returns a series of ordered pairs from a given function

    f: a python function that takes one numerical input and produces one numerical output
    start: the input to start the computation at
    end: the input to end the computation at
    n: the number of points to compute"""
    step:Number=(end-start)/(n-1)
    points:tuple=()
    for i in range(n):
        x:Number=i*step
        y:Number=f(x)
        points=points+((x,y),)
    return points
def function_lines(f,start:Number,end:Number,n:int=100)->tuple[tuple[Number,Number],...]:
    """function_lines(f, start, end, n=100) Returns a series of lines (length, heading) approximating a function

    f: a python function that takes one numerical input and produces one numerical output
    start: the input to start the computation at
    end: the input to end the computation at
    n: the number of lines to compute"""
    points:tuple=function_points(f,start,end,n+1)
    lines:tuple=()
    #iterates through every element in points except the last
    for index, point in enumerate(points[0:-1]):
        x1:Number=point[0]
        y1:Number=point[1]
        x2:Number=points[index+1][0]
        y2:Number=points[index+1][1]
        length=sqrt((x2-x1)**2+(y2-y1)**2)
        slope:Number=(y2-y1)/(x2-x1)
        radian_heading=atan(slope)
        heading=radian_heading*180/pi
        lines = lines+((length,heading),)
    return lines
def sym_dict(dictionary:dict)->dict:
    """sym_dict(dictionary) Makes a dictionary symmetrical, if (x:y) then (y:x)

    dictionary: the dictionary to be made symmetrical"""
    #the original dictionary must not be affected
    return_dict:dict=dictionary.copy()
    for key in dictionary.keys():
        return_dict[return_dict[key]] = key
    return return_dict
letter_equivalents:dict=sym_dict({'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J'
    ,'k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X'
    ,'y':'Y','z':'Z'})
def same_letter(char1:str,char2:str)->bool:
    """same_letter(char1, char2) Checks if two characters are the same, ignoring capitalization

    char1: one of the characters to be compared
    char2: the other character to be compared"""
    if char1 in letter_equivalents:
        return char1==char2 or letter_equivalents[char1]==char2
    #if the char1 is not a letter, check for simple equality
    else:
        return char1 == char2
def same_letters(str1: str,str2:str)->bool:
    """same_letters(str1, str2) Checks whether two strings are the same, ignoring capitalization

    str1: one of the strings
    str2: the other string"""
    #if the strings are different lengths, there is no need to continue
    if len(str1)!=len(str2):
        return False
    index:int=0
    while index<len(str1):
        if not same_letter(str1[index],str2[index]):
            return False
        index =index+1
    return True