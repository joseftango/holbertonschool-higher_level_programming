#!/usr/bin/python3
"""2-matrix_devided m"""


def matrix_divided(matrix, div):
    """function that divid two numbers int or float"""
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix \
                        (list of lists) of integers/floats')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    new_list = []
    for r in matrix:
        if type(r) is not list:
            raise TypeError('matrix must be a matrix \
                            (list of lists) of integers/floats')
        for c in r:
            if type(c) not in [int, float]:
                raise TypeError('matrix must be a matrix \
                                (list of lists) of integers/floats')
            new_list.append(round(c / div, 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
