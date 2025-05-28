#!/usr/bin/python3
"""
This module provides a class BaseGeometry
"""


class BaseGeometry:
    """
    This class is about geometry
    """

    def area(self):
        """
        Raise an exception as area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
