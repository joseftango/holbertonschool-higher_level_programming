#!/usr/bin/python3
for n in range(0, 100):
    if n == 100 - 1:
        print('{:02}'.format(n))
    else:
        print('{:02}'.format(n), end=', ')
