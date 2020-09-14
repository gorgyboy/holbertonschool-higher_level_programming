#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    operators = ['+', '-', '*', '/']

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if argv[2] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a, b = int(argv[1]), int(argv[3])

    if argv[2] == '+':
        c = add(a, b)
    elif argv[2] == '-':
        c = sub(a, b)
    elif argv[2] == '*':
        c = mul(a, b)
    else:
        c = div(a, b)

    print('{:d} {} {:d} = {:d}'.format(a, argv[2], b, c))
