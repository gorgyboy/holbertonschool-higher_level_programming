#!/usr/bin/python3
from sys import argv
arg_len = len(argv)

if __name__ == "__main__":
    if arg_len == 1:
        print('0 arguments.')
    else:
        if arg_len == 2:
            print('1 argument:')
        else:
            print('{:d} arguments:'.format(arg_len - 1))
        for i in range(1, arg_len):
            print('{:d}: {}'.format(i, argv[i]))
