#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered by attrs."""
        if type(attrs) is not list:
            return self.__dict__
        else:
            dic_vide = {}

            for i in range(attrs):
                if i == hasattr(self, nom):
                    dic_vide += getattr(self, nom)
