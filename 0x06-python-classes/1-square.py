#!/usr/bin/python3
"""A module on private instance creation in classes, python oop"""


class Square:
    """An class that defines a square and it's size"""

    def __init__(self, size):
        """initializing attributes"""
        self.__size = size
