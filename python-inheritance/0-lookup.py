#!/usr/bin/python3
"""
Module with a function to list attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns list of available attributes and methods.
    """
    return dir(obj)
