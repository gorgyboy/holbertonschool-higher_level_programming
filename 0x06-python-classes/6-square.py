#!/usr/bin/python3


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialized the square.

        Args:
            size (int): Size to create the square, defautls to 0.
            position (tuple, int): Cordinates to create the square, 
                defaults to (0,0).

        Attributes:
            __size (int): Private, size of the square.
            __position (tuple, int): Private, cordinates of the square.

        """

        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        err = TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple:
            raise err
        elif len(value) != 2:
            raise err
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise err
        elif value[0] < 0 or value[1] < 0:
            raise err
        else:
            self.__position = value

    def area(self):
        """Calculates the square's area.

        Returns:
            __size^2.

        """
        return self.__size ** 2

    def my_print(self):
        if self.size:
            for pos_y in range(self.position[1]):
                print()
            for row in range(self.size):
                for pos_x in range(self.position[0]):
                    print(" ", end='')
                for col in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
