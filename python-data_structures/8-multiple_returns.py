#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = ''
    strlen = 0
    if sentence == '':
        first_char = None
    else:
        strlen = len(sentence)
        first_char = sentence[0]
    return strlen, first_char
