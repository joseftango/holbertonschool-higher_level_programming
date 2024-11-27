#!/usr/bin/python3
i = 0
while i < 100:
    if i / 10 < i % 10:
        if i == 89:
            print('{:0=2d}'.format(i))
        else:
            print('{:0=2d}'.format(i), end=', ')
    i += 1
