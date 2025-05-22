#!/usr/bin/python3
"""
Defines a Rectangle class with width and height.
"""


class Rectangle:
    """
    Rectangle with width and height.
    Tracks number of instances.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Init rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return rectangle as string.
        """
        if self.height == 0 or self.width == 0:
            return ""
        line = str(self.print_symbol) * self.width
        lines = [line] * self.height
        return '\n'.join(lines)

    def __repr__(self):
        """
        Return repr for eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Print message on delete.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return bigger rectangle or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
