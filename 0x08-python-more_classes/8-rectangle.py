#!/usr/bin/python3
""" 8th Task """


class Rectangle:
    """
        Create Class methods
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Initialie width and height
        """
        Rectangle.number_of_instances += 1
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
            result += (str(self.print_symbol) * self.width) + '\n'
        return result.rstrip('\n')

    def __repr__(self) -> str:
        """
            return a string representation
        """
        return f"Rectangle({self.width}, {self.height})"

    def eval():
        return Rectangle.__str__

    def bigger_or_equal(rect_1, rect_2):
        """
            returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_2.area() == rect_1.area():
            return rect_1
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        # return max(rect_1.area(), rect_2.area())

    def __del__(self):
        """
        While deleting
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
