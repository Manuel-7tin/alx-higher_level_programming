#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unit = number % 10
if number < 0:
    unit -= 10
if unit == 0:
    print("Last digit of {1} is {0} and is 0".format(unit, number))
elif unit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, unit))
elif unit < 6:
    print(f"Last digit of {number} is {unit} and is less than 6 and not 0")
