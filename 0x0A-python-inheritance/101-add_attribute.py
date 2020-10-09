#!/usr/bin/python3
''' 0x0A-python-inheritance module '''


def add_attribute(obj, name, value):
    ''' Adds a new attribute to obj '''

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
