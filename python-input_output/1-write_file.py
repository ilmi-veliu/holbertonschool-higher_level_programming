#!/usr/bin/python3
"""a function that writes a string to a text file
and returns the numnber of characters written"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file
    and returns the numnber of characters written"""
    with open(filename, 'w') as file:
        file.write(text)
        return len(text)
