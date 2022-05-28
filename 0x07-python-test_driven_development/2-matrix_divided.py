#!/usr/bin/python3
"""(__import__("2-matrix_divided.py").__doc__)"""
def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""
    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) is 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    if size is 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) is not size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    return [[round(b / div, 2) for b in i] for i in matrix]
