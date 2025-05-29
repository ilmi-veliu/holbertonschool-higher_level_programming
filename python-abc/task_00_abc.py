#!/usr/bin/env python3
"""
Module task_00_abc
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This abstract class provides animal
    """

    @abstractmethod
    def sound(self):
        """
        Describes a sound for an animal
        """

        pass


class Dog(Animal):
    """
    This subclass provides a dog
    """

    def sound(self):
        """
        Returns the sound of a dog
        """

        return "Bark"


class Cat(Animal):
    """
    This subclass provides a cat
    """

    def sound(self):
        """
        Returns the sound of a cat
        """

        return "Meow"
