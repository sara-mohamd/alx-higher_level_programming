#!/usr/bin/python3
""" Q2 """


def matrix_divided(matrix, div):
    """..."""
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix[1:]:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("div must be a number")

    result = []
    for i in range(len(matrix)):

        result.append([round(x/div, 2) for x in matrix[i]])
    return result
