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