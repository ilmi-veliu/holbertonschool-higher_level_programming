#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods to calculate area
and validate integer values.
"""


class BaseGeometry:
    """A class representing the base of geometry objects."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
