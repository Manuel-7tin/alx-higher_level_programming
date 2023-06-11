#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for listt in matrix:
        for num in listt:
            print("{:d}".format(num), end=" ")
        print()


