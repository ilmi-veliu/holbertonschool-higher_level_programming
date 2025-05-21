#!/usr/bin/python3
"""Module rectangle

Ce module définit une classe Rectangle permettant
de créer des objets rectangles avec une largeur (width)
et une hauteur (height), tout en contrôlant la validité des valeurs.
"""

class Rectangle:
    """Classe Rectangle définissant un rectangle avec largeur et hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): largeur du rectangle (par défaut 0)
            height (int): hauteur du rectangle (par défaut 0)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retourne la largeur du rectangle.

        Returns:
            int: largeur actuelle du rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): nouvelle valeur de la largeur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur du rectangle.

        Returns:
            int: hauteur actuelle du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.

        Args:
            value (int): nouvelle valeur de la hauteur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
