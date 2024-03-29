#!/usr/bin/python3
"""creation of pascal_triangle function"""


def pascal_triangle(n):
    """function that returns a list of lists of
    integers representing the Pascal’s triangle of n"""
    tree = [[1]]
    for x in range(1, n):
        m = [1]
        for y in range(1, x):
            m.append(tree[x-1][y-1] + tree[x-1][y])
        m.append(1)
        tree.append(m)
    return tree
