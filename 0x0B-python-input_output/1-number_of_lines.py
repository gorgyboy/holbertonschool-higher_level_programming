#!/usr/bin/python3
''' I/O module '''


def number_of_lines(filename=""):
    ''' Returns the number of lines of a text file '''

    with open(filename, mode='r', encoding='utf-8') as f:
        nb_lines = 0
        for line in f:
            nb_lines += 1
    return nb_lines
