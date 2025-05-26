#!/usr/bin/python3
"""
Module that defines the lookup function.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attributes and methods.
    """
    return dir(obj)
