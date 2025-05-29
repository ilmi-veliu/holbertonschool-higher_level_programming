#!/usr/bin/python3
"""
This module defines BaseGeometry, Rectangle, and Square classes.
"""


class BaseGeometry:
    """Basic geometry validation."""

    def area(self):
        """
        Raise an Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle shape, inherits BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: String with width and height.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square shape, inherits Rectangle."""

    def __init__(self, size):
        """
        Initialize square with size.

        Args:
            size (int): The length of the sides of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: Inherited string representation from Rectangle.
        """
        return "[Square] {}/{}".format(self.__size,self.__size)
