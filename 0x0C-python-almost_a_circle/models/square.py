#!/usr/bin/python3
""" Models module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the instance.

            Attributes:
                size (int): Size of the instance, which is width and height.
                x (int):    x axis position of the instance.
                y (int):    y axis position of the instance.
                id (int):   Instance id. If None,  _base.__nb_objects will
                            be increased and used as id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns __width as size. """
        return self.width

    @size.setter
    def size(self, value):
        """ Verifies that value is int and greater than 0
            and assign it to width and height.
        """
        if type(value) is not int:
            raise TypeError('width must be integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id,
                self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update instance attributes, receiving *args as id, size, x and y.
            **kwargs is only used if *args is empty.
        """
        if args:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance. """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
