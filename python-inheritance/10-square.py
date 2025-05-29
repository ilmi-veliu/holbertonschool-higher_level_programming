#!/usr/bin/python3
"""
This module provides the Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes an instance with size
        """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns the rectangle description
        """

        return ("[Square] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Returns the square area
        """

        return self.__size * self.__size