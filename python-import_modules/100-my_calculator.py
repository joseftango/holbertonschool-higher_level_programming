#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


if __name__ == '__main__':
    num_of_args = len(argv) - 1
    if num_of_args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = str(argv[2])
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if op not in ops.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}'.format(a, op, b, ops[op](a, b)))
