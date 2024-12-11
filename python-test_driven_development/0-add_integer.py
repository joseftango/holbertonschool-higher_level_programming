#!/usr/bin/python3
"""0-add_integer module"""


def add_integer(a, b=98):
    """addition of two numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)

    return a + b
