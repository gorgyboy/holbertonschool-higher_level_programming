#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_matrix = [[matrix[row][col] ** 2 for col in
                     range(len(matrix[row]))] for row in range(len(matrix))]
    return square_matrix
