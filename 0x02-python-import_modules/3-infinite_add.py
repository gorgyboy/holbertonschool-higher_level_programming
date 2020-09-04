#!/usr/bin/python3
from sys import argv
res = 0
first = True

if __name__ == "__main__":
    for num in argv:
        if first:
            first = False
        else:
            res = res + int(num)
    print('{}'.format(res))
