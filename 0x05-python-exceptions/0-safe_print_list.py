#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print()
            return element_num
        else:
            element_num += 1
    print()
    return element_num
