#!/usr/bin/python3
"""
This module defines a class BaseGeometry
with a public method area that raises an Exception.
"""


class BaseGeometry:
    """
    A class that represents geometry base.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        Raises:
            Exception: Always raised with the message.
        """
        raise Exception("area() is not implemented")
