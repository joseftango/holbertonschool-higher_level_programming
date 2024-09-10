#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv
num_of_args = len(argv[1:])
if num_of_args != 3:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)

num1 = int(argv[1])
num2 = int(argv[3])
op = argv[2]

if op in '+-*/':
    if op == '+':
        print('{} {} {} = {}'.format(num1, op, num2, add(num1, num2)))
    elif op == '-':
        print('{} {} {} = {}'.format(num1, op, num2, sub(num1, num2)))
    elif op == '*':
        print('{} {} {} = {}'.format(num1, op, num2, mul(num1, num2)))
    else:
        print('{} {} {} = {}'.format(num1, op, num2, div(num1, num2)))
else:
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
