#!/usr/bin/python3
"""4-print_square = __import__("4-print_square").__doc__)"""


def print_square(size):
    """function that prints a square with #"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
