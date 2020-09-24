#!/usr/bin/python3

"""Square module"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): Size to create the square, defautls to 0.

        Attributes:
            __size (int): Private, size of the square.

        """

        self.size = size

    @property
    def size(self):
        """Sets and gets the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Verifies that size is integer and bigger than zero."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square's area.

        Returns:
            Square's area.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout represented by '#'."""
        if self.size:
            for row in range(self.size):
                for col in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
