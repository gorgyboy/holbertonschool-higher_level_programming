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

        if attrs and isinstance(attrs, list) \
        and all(isinstance(a, str) for a in attrs):
            d_list = self.__dict__
            d_attrs = dict()
            for key in attrs:
                if key in d_list:
                    d_attrs[key] = d_list[key]
            return d_attrs
        else:
            return self.__dict__
