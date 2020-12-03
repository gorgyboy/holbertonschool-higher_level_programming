#!/usr/bin/python3
"""
4-print_square module
"""


def print_square(size):
    """
    Prints a square with the character #
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
