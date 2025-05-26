#!/usr/bin/python3

def lookup(obj):
    """
    lookup - returns list of available attributes and methods
    @obj: object to inspect
    Return: list of attributes and methods
    """
    return dir(obj)
