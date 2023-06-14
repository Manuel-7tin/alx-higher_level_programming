#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    temp_list = []
    for num in my_list:
        if num not in temp_list:
            sum += num
            temp_list.append(num)
    return sum
