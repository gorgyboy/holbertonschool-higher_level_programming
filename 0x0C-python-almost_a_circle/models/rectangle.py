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
                id (int):       Instance id. If None, _Base.__nb_objects will
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
        """ Verifies that value is int and greater than 0. """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Sets and returns height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Verifies that value is int and greater than 0. """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ Sets and returns x. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Verifies that value is int and not less than 0. """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Sets and returns y. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Verifies that value is int and not less than 0. """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Returns the area value of the instance. """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the instance with the character #
            by taking care of x and y.
        """
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for width in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update instance attributes, receiving *args as id, width,
            height, x and y. **kwargs is only used if *args is empty.
        """
        if args:
            for index in range(len(args)):
                if index == 0:
                    self.id = args[index]
                elif index == 1:
                    self.width = args[index]
                elif index == 2:
                    self.height = args[index]
                elif index == 3:
                    self.x = args[index]
                elif index == 4:
                    self.y = args[index]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance. """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
