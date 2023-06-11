#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for num in range(len(my_list)):
        if num != idx:
            new_list.append(my_list[num])
    return new_list
