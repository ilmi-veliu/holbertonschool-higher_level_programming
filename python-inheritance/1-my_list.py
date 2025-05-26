#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        panda = sorted(self)
        print(panda)
