#!/usr/bin/python3


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialized the square.

        Args:
            size (int): Size to create the square, defautls to 0.

        Attributes:
            __size (int): Private, size of the square.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the square's area.

        Returns:
            __size^2.

        """
        return self.__size ** 2
