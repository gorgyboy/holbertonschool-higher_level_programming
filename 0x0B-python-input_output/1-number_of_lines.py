#!/usr/bin/python3


def number_of_lines(filename=""):
    ''' Returns the number of lines of a text file '''

    with open(filename, 'r') as f:
        nb_lines = 0
        for line in f:
            nb_lines += 1
    return nb_lines
