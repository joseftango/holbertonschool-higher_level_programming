#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '' or sentence == None:
        return 0, 0
    return len(sentence), sentence[0]
