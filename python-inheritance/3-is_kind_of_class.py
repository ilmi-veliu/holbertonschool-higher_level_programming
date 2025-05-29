#!/usr/bin/python3
"""
This module provides a function that returns
if an object is from a specific class or not
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is from the specified class,
    otherwise return false
    """

    return isinstance(obj, a_class)
