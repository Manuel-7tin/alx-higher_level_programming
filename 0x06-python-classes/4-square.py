#!/usr/bin/python3
"""A module on getter and setter creation in classes, python oop"""


class Square:
    """A class that defines a square and creates a getter and setter for it"""

    def __init__(self, size=0):
        """getter and setter creation"""
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
