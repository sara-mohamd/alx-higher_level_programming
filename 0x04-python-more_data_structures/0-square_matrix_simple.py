#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
    c = []
    for i in range(len(matrix)):
        temp = []
        for j in range(0, len(matrix[i])):
            temp.append(matrix[i][j] * matrix[i][j])
        c.append(temp)
    return c
