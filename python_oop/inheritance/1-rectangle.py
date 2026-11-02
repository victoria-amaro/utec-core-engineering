#!/usr/bin/env python3
"""
Módulo que define la clase Rectangle que hereda de BaseGeometry.
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
