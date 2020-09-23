#!/usr/bin/python3

"""Square module"""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square.

        Args:
            size (int): Size to create the square.

        Attributes:
            __size (int): Private, size of the square.

        """
        self.__size = size
