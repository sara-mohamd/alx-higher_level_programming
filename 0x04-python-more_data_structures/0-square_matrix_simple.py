#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    c = []
    for i in matrix:
        c.append(list(map(lambda i: i**2, i)))
    return c

