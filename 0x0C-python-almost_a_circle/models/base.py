#!/usr/bin/python3
""" Models module """

from json import dumps, loads
from csv import writer, reader


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

    @staticmethod
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

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.

            Attributes:
                json_string (str): String representing a list of dictionaries.
        """
        if json_string:
            return loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.

            Attributes:
                list_objs (list): List of instances who inherits of Base.
        """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            f.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from <cls.__name__>.json file. """
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_insts = []
                list_dicts = cls.from_json_string(f.read())
                for dic in list_dicts:
                    list_insts.append(cls.create(**dic))
                return list_insts
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set.

                Attributes:
                    **dictionary (dict): Dictionary with the values of the
                                       instance to be created.
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Writes the CSV string representation of list_objs to a file.

            Attributes:
                list_objs (list): List of instances who inherits of Base.
        """
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8',
                  newline='') as csv_f:
            csv_writer = writer(csv_f)
            if cls.__name__ is 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            else:
                fields = ['id', 'size', 'x', 'y']
            values = []
            for obj in list_objs:
                obj_attrs = []
                for attr in fields:
                    obj_attrs.append(getattr(obj, attr))
                values.append(obj_attrs)
            csv_writer.writerow(fields)
            csv_writer.writerows(values)

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances from <cls.__name__>.csv file. """
        try:
            with open(cls.__name__ + '.csv', 'r', encoding='utf-8',
                      newline='') as csv_f:
                csv_reader = reader(csv_f)
                fields = next(csv_reader)
                values = []
                for line in csv_reader:
                    values.append([int(attr) for attr in line])
                list_dicts = []
                for index in range(len(values)):
                    list_dicts.append(dict(zip(fields, values[index])))
                list_insts = []
                for dic in list_dicts:
                    list_insts.append(cls.create(**dic))
                return list_insts
        except FileNotFoundError:
            return []
