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
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """hat prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size + 1):
                print("#" * self.__size)
        else:
            print()
