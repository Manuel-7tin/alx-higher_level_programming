#!/usr/bin/python3
for tens in range(0, 10):
    for unit in range(tens+1, 10):
        if tens != 8:
            print("{}{}".format(tens, unit), end=", ")
        else:
            print("{}{}".format(tens, unit))
