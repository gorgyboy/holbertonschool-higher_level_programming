#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle():
    """
    Recatangle class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance.
        Args:
            width (int): Rectangle's width.
            height (int): Rectangle's height.
        """

        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Return the rectangle's area
        """

        return self.width * self.height

    def perimeter(self):
        """
        Return the rectangle's perimieter
        """

        if 0 in {self.width, self.height}:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """
        Return string representation of the rectangle
        """

        if 0 in {self.width, self.height}:
            return ''

        string = str()
        for i in range(self.height):
            string += '#' * self.width
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        Return an official represention of the rectangle
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Deletes the rectangle
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
