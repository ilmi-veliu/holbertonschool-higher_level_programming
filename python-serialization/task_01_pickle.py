#!/usr/bin/env python3
import pickle


class CustomObject:
    """Custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize object with name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an object from a file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj
        except Exception:
            return None

    def display(self):
        """Print object attributes."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)
