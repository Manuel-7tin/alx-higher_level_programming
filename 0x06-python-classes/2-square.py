#!/usr/bin/python3
"""A module on private instance validation in classes, python oop"""


class Square:
    """A class that defines a square and validates it's size"""

    def __init__(self, size=0):
        """attributes validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
