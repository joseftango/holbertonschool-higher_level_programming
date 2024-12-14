#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """prints a square using # character base from size"""
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for r in range(size):
        for c in range(size):
            print('#', end='')
        print()
