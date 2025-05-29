#!/usr/bin/python3
"""Module defining an abstract Animal class and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses to produce a sound."""
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Returns the sound made by a dog."""
        return "BARK"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Returns the sound made by a cat."""
        return "Meow"
