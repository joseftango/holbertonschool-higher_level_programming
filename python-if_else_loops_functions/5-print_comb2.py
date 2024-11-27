#!/usr/bin/python3
i = 0
while i < 100:
    if i == 99:
        print('{:0=2d}'.format(i))
    else:
        print('{:0=2d}'.format(i), end=', ')
    i += 1
