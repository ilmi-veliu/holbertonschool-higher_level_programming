#!/usr/bin/python3
"""
Module 5-square

This module defines a Square class to represent a square by its size.
"""


class Square:
    """
    Class that defines a square by its size and provides methods
    to calculate the area and print the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square. Must be a non-negative integer.
        """
        self.size = size  # utilisation du setter

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#'.

        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
