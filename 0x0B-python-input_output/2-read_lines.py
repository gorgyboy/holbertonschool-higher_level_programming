#!/usr/bin/python3
''' I/O module '''


def read_lines(filename="", nb_lines=0):
    ''' Reads n lines of a text file (UTF8) and prints it to stdout.
        Reads the entire file if nb_lines is lower or equal to 0
        OR greater or equal to the total number of lines of the file.
    '''

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = list(f)
        if nb_lines <= 0 or nb_lines >= len(lines):
            for i in range(len(lines)):
                print(lines[i], end='')
        else:
            for i in range(nb_lines):
                print(lines[i], end='')
