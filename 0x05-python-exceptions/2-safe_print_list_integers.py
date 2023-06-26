#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element_num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            pass
        except TypeError:
            pass
        else:
            element_num += 1
    print()
    return element_num
