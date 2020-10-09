#!/usr/bin/python3
''' 0x0A-python-inheritance module '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square class that inherits from Rectangle class '''

    def __init__(self, size):
        ''' Initializes an instance '''

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Returns the area '''

        return self.__size ** 2

    def __str__(self):
        ''' Returns instance representation '''

        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
