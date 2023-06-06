#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        char_case = ords(char)
        if char_case > 96 and char_case < 123:
            upper_str += chr(char_case - 32)
        else:
            upper_str += char
    print(upper_str)
