#!/usr/bin/env python3
"""
Módulo que define la clase Rectangle con cálculo de área y perímetro.
"""


class Rectangle:
    """
    Representa un rectángulo con ancho, alto, área y peretro.
    """

    def __init__(self, width=0, height=0):
        """
        Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): El ancho del rectángulo. Por defecto 0.
            height (int): El alto del rectángulo. Por defecto 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter para width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter para width con validación de tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter para height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter para height con validación de tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula y devuelve el perímetro del rectángulo."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
