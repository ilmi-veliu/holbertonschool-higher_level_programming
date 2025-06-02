#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as p:
        print(p.read())
