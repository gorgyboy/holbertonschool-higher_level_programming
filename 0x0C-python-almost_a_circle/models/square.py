#!/usr/bin/python3
""" Models module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the instance.

            Attributes:
                __size (int):   Size of the instance.
                __x (int):      x axis position of the instance.
                __y (int):      y axis position of the instance.
                id (int):       Instance id. If None,  _base.__nb_objects will
                                be increased and used as id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id,
                self.x, self.y, self.width)
