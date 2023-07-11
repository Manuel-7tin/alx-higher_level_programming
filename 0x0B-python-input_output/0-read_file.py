#!/usr/bin/python3
"""
This module  illustrates the act of reading frtom a file
"""


def read_file(filename=""):
    """
    read_file - function: Takes in a file name and prints out the file content.
    """

    with open(filename) as file:
        print(file.read(), end="")
