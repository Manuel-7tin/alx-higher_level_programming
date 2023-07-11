#!/usr/bin/python3
"""
This module  demonstrates the act of writing to a file
"""


def write_file(filename="", text=""):
    """
    write_file - function: Takes in a file name and writes some content
    to the file
    returns number of char.
    """

    with open(filename, mode="w") as file:
        return file.write(text)
