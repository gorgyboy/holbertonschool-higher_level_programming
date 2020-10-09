#!/usr/bin/python3
''' 0x0A-python-inheritance module '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class that inherits from BaseGeometry class '''

    def __init__(self, width, height):
        ''' Initializes an instance '''

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        self.__width = width
