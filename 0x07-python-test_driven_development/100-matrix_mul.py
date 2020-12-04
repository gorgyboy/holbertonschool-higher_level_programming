#!/usr/bin/python3
"""
Matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices.

    Args:
        m_a - m_b: list of lists that must contain int or float values.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(m_list, list) for m_list in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(m_list, list) for m_list in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not all(m_list for m_list in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(m_list for m_list in m_b):
        raise ValueError("m_b can't be empty")

    for m_list in m_a:
        if not all(isinstance(l_value, (int, float)) for l_value in m_list):
            raise TypeError("m_a should contain only integers or floats")
    for m_list in m_b:
        if not all(isinstance(l_value, (int, float)) for l_value in m_list):
            raise TypeError("m_b should contain only integers or floats")

    for idx in range(len(m_a) - 1):
        if len(m_a[idx]) != len(m_a[idx + 1]):
            raise TypeError("each row of m_a must be of the same size")
    for idx in range(len(m_b) - 1):
        if len(m_b[idx]) != len(m_b[idx + 1]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res_matrix = []
    for row in range(len(m_a)):  # rows in res_matrix
        res_list = []
        for col in range(len(m_b[0])):  # cols in res_matrix
            res_value = 0
            # itare in the same row/col
            for pos in range(len(m_b[0])):
                # multiply and add values to res_list
                res_value += (m_a[row][pos] * m_b[pos][col])
            res_list.append(res_value)
        res_matrix.append(res_list)  # add res_list to res_matrix
    return res_matrix
