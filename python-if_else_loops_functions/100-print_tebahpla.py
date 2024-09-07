#!/usr/bin/python3
for j in range(90, 64, -1):
    if j % 2 == 0:
        j += 32
    print('{}'.format(chr(j)), end='')
