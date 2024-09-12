#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_sum = 0
    weight_sum = 0
    for s, w in my_list:
        score_sum += s * w
        weight_sum += w
    return score_sum / weight_sum if weight_sum != 0 else 0
