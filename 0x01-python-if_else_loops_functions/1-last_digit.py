#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p_number = number
if p_number < 0:
    p_number *= -1
last_digit = number % 10
if last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif last_digit > 5:
    print("Last digit of {1} is {0} and is greater than 5".format(last_digit, number))
elif last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
