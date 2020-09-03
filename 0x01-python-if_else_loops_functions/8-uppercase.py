#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= 97 and c <= 122:
            c = c - 32
        print('{:c}'.format(c), end='')
    print()
