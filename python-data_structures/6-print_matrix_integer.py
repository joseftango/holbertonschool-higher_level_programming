#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i in range(len(r)):
            if i == len(r) - 1:
                print('{:d}'.format(r[i]), end='')
            else:
                print('{:d}'.format(r[i]), end=' ')
        print()
