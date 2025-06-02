#!/usr/bin/python3
"""Append a string at the end of a file and return the number of characters written"""

def append_write(filename="", text=""):
    """Append text to a file and return number of characters written"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
