#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        maxm = key
        break
    for key1 in a_dictionary:
        for key2 in a_dictionary:
            if a_dictionary[key1] < a_dictionary[key2]:
                break
            elif a_dictionary[key1] > a_dictionary.get(maxm):
                maxm = key1
    return maxm
