#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


a = 10
b = 5
ops = [add, sub, mul, div]
sumbol = '+-*/'

for i in range(len(ops)):
    print('{} {} {} = {}'.format(a, sumbol[i], b, ops[i](a, b)))
