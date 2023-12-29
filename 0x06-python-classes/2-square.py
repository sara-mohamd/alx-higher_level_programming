#!/usr/bin/python3

"""New Module"""


class Square:
    """Task"""

    def __init__(self, size=0):
        """
        Private instance attribute
        write size with rules
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
