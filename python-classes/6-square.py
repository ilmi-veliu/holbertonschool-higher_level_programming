#!/usr/bin/python3
"""
Defines a Square class with size and position attributes,
and methods to compute area and print the square.
"""


class Square:
    """
    Represents a square defined by its size and print position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): Optional size of the square (default 0). Must be a non-negative integer.
            position (tuple): Optional position offset (default (0, 0)). 
                Must be a tuple of two non-negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): New side length to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the printing position of the square.

        Returns:
            tuple: Two non-negative integers representing horizontal and vertical offsets.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the printing position of the square with validation.

        Args:
            value (tuple): New position to assign.

        Raises:
            TypeError: If value is not a tuple of two non-negative integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area calculated as size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If size is 0, prints an empty line. Otherwise:
          - Prints each row of the square as '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
