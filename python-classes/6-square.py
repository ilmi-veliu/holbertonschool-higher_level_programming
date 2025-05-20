#!/usr/bin/python3
"""Square class with size and position."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set square position."""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(v, int) and v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return square area."""
        return self.__size ** 2

    def my_print(self):
        """Print square with '#' and position offset."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
