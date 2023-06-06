#!/usr/bin/python3
for num in range(122, 96, -2):
    print("{1}{0}".format(chr(num - 33), chr(num)), end="")
