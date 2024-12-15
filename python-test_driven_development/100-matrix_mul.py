#!/usr/bin/python3
"""100-matrix_mul module"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    column_size_m_a = len(m_a[0])
    column_size_m_b = len(m_b[0])

    for r in m_a:
        if not isinstance(r, list):
            raise TypeError('m_a must be a list of lists')
        if len(r) != column_size_m_a:
            raise TypeError('each row of m_a must be of the same size')
        for c in r:
            if not isinstance(c, (int, float)):
                raise TypeError('m_a should contain only integers or floats')

    for r in m_b:
        if not isinstance(r, list):
            raise TypeError('m_b must be a list of lists')
        if len(r) != column_size_m_b:
            raise TypeError('each row of m_b must be of the same size')
        for c in r:
            if not isinstance(c, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    num_of_colums_left = len(m_a[0])

    num_of_rows_right = len(m_b)

    if num_of_colums_left != num_of_rows_right:
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for j in m_b[0]] for i in m_a]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]

    return res
