#!/usr/bin/python3
''' 0x0A-python-inheritance module '''


class BaseGeometry:
    ''' BaseGeometry class '''

    def area(self):
        ''' Rises an Exception with the message '''

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' Validates value '''

        if type(value) is int:
            if value <= 0:
                raise ValueError('{} must be greater than 0'.format(name))
        else:
            raise TypeError('{} must be an integer'.format(name))


class Rectangle(BaseGeometry):
    ''' Rectangle class that inherits from BaseGeometry class '''

    def __init__(self, width, height):
        ''' Initializes an instance '''

        if self.integer_validator('width', width):
            self.__width = width
        if self.integer_validator('height', height):
            self.__height = height
