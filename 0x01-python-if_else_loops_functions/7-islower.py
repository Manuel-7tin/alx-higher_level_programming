#!/usr/bin/python3
def islower(c):
    unicode_int = ord(c)
    if unicode_int > 96 and unicode_int < 123:
        return True
    else:
        return False
