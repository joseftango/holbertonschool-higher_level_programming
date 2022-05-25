#!/usr/bin/python3
"""(__import__("0-add_integer").__doc__)"""

def add_integer(a, b=98):
    """function that add two integer"""
    if type(a) == int or type(a) == float: 
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) == int or type(b) == float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
