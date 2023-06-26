#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp_value = 0
    for i in range(list_length):
        try:
            temp_value = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            temp_value = 0
        except ZeroDivisionError:
            print("division by 0")
            temp_value = 0
        except IndexError:
            print("out of range")
            return new_list
        finally:
            new_list.append(temp_value)
    return new_list
