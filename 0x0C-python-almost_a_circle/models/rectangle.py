#!/usr/bin/python3
""" Models module """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base class. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the instance.

            Attributes:
                __width (int):  Width of the instance.
                __height (int): Height of the instance.
                __x (int):      x axis position of the instance.
                __y (int):      y axis position of the instance.
                id (int):       Instance id. If None, _base.__nb_objects will
                                be increased and used as id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Sets and returns width. """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ Sets and returns height. """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ Sets and returns x. """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ Sets and returns y. """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
