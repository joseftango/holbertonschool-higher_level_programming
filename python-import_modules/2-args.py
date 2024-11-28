#!/usr/bin/python3
from sys import argv


num_of_args = len(argv) - 1

if num_of_args == 0:
    print('{} arguments.'.format(num_of_args))
elif num_of_args == 1:
    print('{} argument:'.format(num_of_args))
    print('1: {}'.format(argv[1]))
else:
    print('{} arguments:'.format(num_of_args))
    for i in range(1, num_of_args + 1):
        print('{}: {}'.format(i, argv[i]))
