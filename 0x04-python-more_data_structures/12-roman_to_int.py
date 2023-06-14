#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    for num in range(len(roman_string)):
        current_number = rom_num[roman_string[num]]
        if num != len(roman_string)-1:
            next_number = rom_num[roman_string[num+1]]
            if current_number < next_number:
                number -= current_number
            else:
                number += current_number
        else:
            number += current_number
    return number
