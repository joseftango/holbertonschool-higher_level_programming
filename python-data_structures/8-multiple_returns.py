#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return None, len(sentence)
    return len(sentence), sentence[0]
