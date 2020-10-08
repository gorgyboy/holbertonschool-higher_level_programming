#!/usr/bin/python3
''' I/O module '''


class Student():
    """
    Class representing a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a class object
        """
        self.first_name = first_name,
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of a class object
        """
        return self.__dict__
