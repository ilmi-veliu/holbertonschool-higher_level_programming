#!/usr/bin/env python3
import pickle


class CustomObject:
    """Custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize object with name, age, and is_student."""
        self.__name = name
        self.__age = age
        self.__is_student = is_student

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an object from a file."""
        with open(filename, "rb") as panda:
            pelo = pickle.load(panda)
            return pelo

    def display(self):
        """Print object attributes."""
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Is Student:", self.__is_student)
