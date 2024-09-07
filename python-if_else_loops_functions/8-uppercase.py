#!/usr/bin/python3
def uppercase(str):
    upper_str = ''
    for i in range(len(str)):
        decimal = ord(str[i])
        if decimal > 96 and decimal < 123:
            upper_str += chr(decimal - 32)
        else:
            upper_str += chr(decimal)

    print('{}'.format(upper_str))
