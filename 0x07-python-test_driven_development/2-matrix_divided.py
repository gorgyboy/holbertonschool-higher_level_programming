#!/usr/bin/python3
"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix by div.
    """

    if not all(isinstance(element, list) for element in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for element in matrix:
        if not all(isinstance(value, (int, float)) for value in element):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for index in range(len(matrix)):
        if index - 1 >= 0:
            if len(matrix[index]) != len(matrix[index - 1]):
                raise TypeError(
                    "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for element in matrix:
        divided_list = []
        for value in element:
            divided_list.append(round(value / div, 2))
        divided_matrix.append(divided_list)
    return divided_matrix
