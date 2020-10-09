#!/usr/bin/python3
''' 0x0A-python-inheritance module '''


def inherits_from(obj, a_class):
    ''' Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    '''

    return issubclass(obj, a_class)
