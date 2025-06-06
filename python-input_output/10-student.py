#!/usr/bin/python3
"""
Module 10-student
"""


class Student():
    """
    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary description for JSON serialization of an object
        """

        if type(attrs) is list:
            attr_dic = {}
            for element in attrs:
                if type(element) is str and hasattr(self, element):
                    attr_dic[element] = getattr(self, element)
            return attr_dic
        else:
            return self.__dict__
