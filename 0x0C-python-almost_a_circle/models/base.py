#!/usr/bin/python3
""" Models module """

import turtle
from json import dumps, loads
from csv import writer, reader
from random import randint


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
        if not list_dictionaries:
            list_dictionaries = []
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.

            Attributes:
                json_string (str): String representing a list of dictionaries.
        """
        if not json_string:
            json_string = "[]"
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.

            Attributes:
                list_objs (list): List of instances who inherits of Base.
        """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            list_dicts = []
            if list_objs:
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_dicts))

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
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares.

            Attributes:
                list_rectangles (list, Rectangle): List of rectangles.
                list_squares (list, Square):       List of squares.
        """
        scr = turtle.Screen()
        scr.title("0x0C. Python - Almost a circle - 21. Let's draw it " +
                  "#advanced")
        turtle.mode("logo")
        turtle.colormode(255)
        pen = turtle.Turtle()
        pen.speed(2)
        for rect in list_rectangles:
            pen.goto(rect.x, rect.y)
            pen.down()
            pen.color(randint(0, 255), randint(0, 255), randint(0, 255))
            pen.begin_fill()
            for i in range(2):
                pen.forward(rect.height)
                pen.right(90)
                pen.forward(rect.width)
                pen.right(90)
            pen.end_fill()
            pen.up()
        for sqr in list_squares:
            pen.goto(sqr.x, sqr.y)
            pen.down()
            pen.color(randint(0, 255), randint(0, 255), randint(0, 255))
            pen.begin_fill()
            for i in range(4):
                pen.forward(sqr.size)
                pen.right(90)
            pen.end_fill()
            pen.up()
        scr.exitonclick()
