#!/usr/bin/python3
def square(num):
    return num ** 2


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for listt in matrix:
        new_matrix.append(list(map(square, listt)))
        print(list(map(square, listt)))
    return new_matrix
