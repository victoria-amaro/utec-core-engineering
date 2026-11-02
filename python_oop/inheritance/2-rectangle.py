#!/usr/bin/env python3
"""
Módulo que define la clase Rectangle completa con área y representación __str__.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Representa un rectángulo definido por width y height.
    """

    def __init__(self, width, height):
        """
        Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): Ancho del rectángulo.
            height (int): Altura del rectángulo.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calcula y devuelve el área del rectángulo.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Devuelve la representación en cadena legible del rectángulo.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
