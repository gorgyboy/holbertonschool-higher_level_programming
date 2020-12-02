#!/usr/bin/python3
"""
add_integer module.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and retuns the result as an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
