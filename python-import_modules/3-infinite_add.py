#!/usr/bin/python3
from sys import argv
res = 0
if len(argv) > 1:
    for i in range(1, len(argv)):
        res += int(argv[i])

if __name__ == '__main__':
    print(res)
