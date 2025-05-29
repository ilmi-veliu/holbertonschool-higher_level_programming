#!/usr/bin/python3
"""Module defining an abstract Shape class and its subclasses Cercle and Rectangle."""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to print area and perimeter of any shape (duck typing)."""
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area:", area)
    print("Perimeter:", perimeter)
