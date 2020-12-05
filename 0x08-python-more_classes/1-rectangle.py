#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle():
    """
    Recatangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance.
        Args:
            width (int): Rectangle's width.
            height (int): Rectangle's height.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Sets and returns width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Verifies that value is int and at least 0
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Sets and returns height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Verifies that value is int and at least 0
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
