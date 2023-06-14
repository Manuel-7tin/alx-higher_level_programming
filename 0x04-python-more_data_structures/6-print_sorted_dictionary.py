#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = []
    for key in a_dictionary:
        key_list.append(key)
    key_list.sort()
    for string in key_list:
        print(f"{string}: {a_dictionary[string]}")
