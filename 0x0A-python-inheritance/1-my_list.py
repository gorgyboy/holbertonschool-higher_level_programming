#!/usr/bin/python3
''' 0x0A-python-inheritance module '''


class MyList(list):
    ''' Class that extends lists '''

    def print_sorted(self):
        ''' Prints the list, but sorted (ascending sort) '''

        print(sorted(self))
