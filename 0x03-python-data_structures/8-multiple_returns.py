#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
        return len(sentence),sentence[0]
    else:
        first_char = sentence[0]
        len_sen = len(sentence)
        my_tuple = (len_sen, first_char)
        return my_tuple
