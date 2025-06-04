#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, filtered if attrs is a list of strings."""
        if type(attrs) is not list:
            return self.__dict__

        dic_vide = {}
        for attr in attrs:
            if hasattr(self, attr):
                dic_vide[attr] = getattr(self, attr)
        return dic_vide
