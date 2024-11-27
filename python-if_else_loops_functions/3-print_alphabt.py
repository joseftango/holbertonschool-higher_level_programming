#!/usr/bin/python3
i = 97
while i < 123:
    if chr(i) != 'e' and chr(i) != 'q':
        print('{}'.format(chr(i)), end='')
    i += 1
