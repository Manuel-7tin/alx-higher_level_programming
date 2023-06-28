#!/usr/bin/python3
"""A module on public method creation in classes, python oop"""


class Square:
    """A class that defines a square and creates a public method for it"""

    def __init__(self, size=0):
        """public method creation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
