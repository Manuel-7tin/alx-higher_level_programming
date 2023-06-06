def print_last_digit(number):
    last_digit = number % 10
    if number < 0:
        last_digit -= 10
        last_digit *= -1
    print("{}".format(last_digit), end="")
    return last_digit
