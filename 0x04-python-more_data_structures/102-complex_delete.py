#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rem_key = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            rem_key.append(key)
    for key in rem_key:
        del a_dictionary[key]
    return a_dictionary
