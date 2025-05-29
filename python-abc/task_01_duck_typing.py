#!/usr/bin/env python3
"""
Module task_01_duck_typing
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This abstract class provides a shape
    """

    @abstractmethod
    def area(self):
        """
        This method provides the area of the shape
        """

        pass

    @abstractmethod
    def perimeter(self):
        """
        This method provides the perimeter of the shape
        """

        pass


class Circle(Shape):
    """
    This subclass provides a circle
    """

    def __init__(self, radius):
        """
        This method initializes a circle
        """

        self.radius = radius

    def area(self):
        """
        This method provides the area of the circle
        """

        return pi * self.radius * self.radius

    def perimeter(self):
        """
        This method provides the perimeter of the circle
        """

        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    This subclass provides a rectangle
    """

    def __init__(self, width, height):
        """
        This method initializes a rectangle
        """

        self.width = width
        self.height = height

    def area(self):
        """
        This method provides the area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """
        This method provides the perimeter of the rectangle
        """

        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    This function gives information about the area and perimeter of the shape
    """

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
    