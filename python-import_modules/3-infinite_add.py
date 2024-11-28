#!/usr/bin/python3
from sys import argv

num_of_args = len(argv) - 1
res = 0

if num_of_args == 0:
    print('{}'.format(num_of_args))
elif num_of_args == 1:
    print('{}'.format(num_of_args))
else:
    for i in range(1, num_of_args + 1):
        res += int(argv[i])
    print('{}'.format(res))
