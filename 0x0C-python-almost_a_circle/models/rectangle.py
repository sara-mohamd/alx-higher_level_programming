#!/usr/bin/python3
""" 2ed Task """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class Constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ Task 4 """

    def area(self):
        """ Calc area """
        return (self.__width * self.__height)

    # Task 5 & 7
    def display(self):
        """
        Print Rectangle instance
        with character (#)
        Taking care of x and y
        """
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    """ Task 6 """
    def __str__(self):
        """ str representation """
        return f"[Rectangle] ({self.id}) "\
            f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    """ Task 8 & 9"""
    def update(self, *args, **kwargs):
        """
        Update the rectangle
        1st arg (id)
        2nd arg (width)
        3rd arg (height)
        4th arg (x)
        5th arg (y)
        "no-keyword argument"
        **kwargs must be skipped if *args exists and is not empty
        """
        if args:
            #       Don't forget pycodestyle
            for arg, attr in zip(args, ['id', '_Rectangle__width',
                                        '_Rectangle__height',
                                        '_Rectangle__x', '_Rectangle__y']):
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
