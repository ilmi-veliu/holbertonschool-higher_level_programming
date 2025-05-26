#!/usr/bin/python3
# Function that returns the list of available attributes and methods of an object

def lookup(obj):
    """
    lookup - returns list of available attributes and methods
    @obj: object to inspect
    Return: list of attributes and methods
    """
    return dir(obj)
