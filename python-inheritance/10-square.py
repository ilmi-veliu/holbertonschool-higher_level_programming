#!/usr/bin/python3
"""
This module defines BaseGeometry, Rectangle, and Square classes.
"""


class BaseGeometry:
    """Basic geometry validation."""

    def area(self):
        """Raise exception: not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle shape, inherits BaseGeometry."""

    def __init__(self, width, height):
        """Initialize width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square shape, inherits Rectangle."""

    def __init__(self, size):
        """Initialize square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String representation of square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Compute area of square."""
        return self.__size * self.__size
