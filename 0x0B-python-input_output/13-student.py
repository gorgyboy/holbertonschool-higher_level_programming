#!/usr/bin/python3
''' I/O module '''


class Student():
    ''' Class representing a student '''

    def __init__(self, first_name, last_name, age):
        ''' Initializes an object '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Returns a dictionary representation.
            If attrs is a list of strings, only attribute names contained in
            this list must be retrieved. Otherwise, all attributes must be
            retrieved
        '''

        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            attrs_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    attrs_dict[key] = self.__dict__[key]
            return attrs_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        ''' Replaces all attributes of the Student instance '''

        for key in json:
            self.__dict__[key] = json[key]
