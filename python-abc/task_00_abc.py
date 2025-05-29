#!/usr/bin/python3
"""Module qui définit une classe abstraite Animal et ses sous-classes Dog et Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Méthode abstraite à implémenter par les sous-classes pour produire un son."""
        pass


class Dog(Animal):
    """Classe représentant un chien."""

    def sound(self):
        """Retourne le son produit par le chien."""
        return "BARK"


class Cat(Animal):
    """Classe représentant un chat."""

    def sound(self):
        """Retourne le son produit par le chat."""
        return "Meow"
