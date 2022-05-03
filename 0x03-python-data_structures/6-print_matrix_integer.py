#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        len_ele = len(matrix[i])-1
        for j in range(len(matrix[i])):
            if j == len_ele:
                print(f"{matrix[i][j]:d}", end="")
            else:
                print(f"{matrix[i][j]:d}", end=" ")
        print()
