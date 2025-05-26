#!/usr/bin/python3
"""
Module that defines the MyList class.
This module defines a class that inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
