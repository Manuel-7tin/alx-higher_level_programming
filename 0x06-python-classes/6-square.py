#!/usr/bin/python3
"""A module on getter and setter creation in classes, python oop"""


class Square:
    """A class that defines a square and creates a getter and setter for it"""

    def __init__(self, size=0, position=(0, 0)):
        """getter and setter creation"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for num in range(self.__position[1]):
                print()
            for num in range(self.__size):
                for num in range(self.__position[0]):
                    print(" ", end="")
                for num in range(self.__size):
                    print("#", end="")
                print()
