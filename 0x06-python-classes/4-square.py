#!/usr/bin/python3

"""New Module"""


class Square:
    """Task"""

    def __init__(self, size=0):

        """
        Private instance attribute
        write size with rules
        """
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val
