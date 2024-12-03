#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = 0
    best = ''
    for k, v in a_dictionary.items():
        if v > biggest:
            biggest = v
            best = k
    return best
