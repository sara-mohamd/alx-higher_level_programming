#!/usr/bin/python3
""" 2ed Task """


class Rectangle:
    """
        Create Class methods
    """

    def __init__(self, width=0, height=0):
        """
            Initialie width and height
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        @getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        @getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Calc Area
        """
        return self.width * self.height

    def perimeter(self):
        """
            Calc perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
            Print the rectangle
        """
        result = ""
        for _ in range(self.height):
            result += ('#' * self.width) + '\n'
        return result.rstrip('\n')
