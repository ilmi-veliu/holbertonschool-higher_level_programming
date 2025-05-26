#!/usr/bin/python3
"""
Module that defines the MyList class.
It provides a subclass of list with a method to
display the elements in sorted order.
"""


class MyList(list):
    """
    A list subclass with an extra `print_sorted` method.
    """

    def print_sorted(self):
        """
        Display the list elements in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
