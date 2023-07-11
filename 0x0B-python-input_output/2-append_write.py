#!/usr/bin/python3
"""
This module demonsrates the act of appending content to the content of a file
"""


def append_write(filename="", text=""):
    """
    This function appens a piece of text to the contents of a fle
    """

    with open(file=filename, mode="a") as file:
        return file.write(text)
