#!/usr/bin/python3
""" Models module """

from json import dumps


class Base:
    """ Base class for future classes in the module.

        Attributes:
            __nb_objects (int): Represents the number of instances created
                                that didn't have an id and works as an id
                                for them.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the instance.

            Attributes:
                id (int): Instance id. If None, __nb_objects will be
                          increased and used as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries.
            Attributes:
                list_dictionaries (list, dict): List of dictionaries to export
                                                to JSON string.
        """
        if list_dictionaries:
            return dumps(list_dictionaries)
        else:
            return '"[]"'
