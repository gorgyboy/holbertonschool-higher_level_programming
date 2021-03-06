#!/usr/bin/python3
''' I/O module '''


def read_file(filename=""):
    ''' Reads a text file (UTF8) and prints it to stdout '''

    with open(filename, mode='r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
