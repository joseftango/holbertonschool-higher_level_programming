#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '' or sentence == None:
        return None
    return len(sentence), sentence[0]
