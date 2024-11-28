#!/usr/bin/python3
ord_chr = 122
i = 0
while i < 26:
    print('{}'.format(chr(ord_chr)), end='')
    if ord_chr >= 97 and ord_chr <= 122:
        ord_chr -= 32
    else:
        ord_chr += 32
    ord_chr -= 1
    i += 1
