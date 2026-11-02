#!/usr/bin/env python3
"""
Módulo que define la clase Square que hereda de Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Representa un cuadrado definido por su tamaño.
    """

    def __init__(self, size):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño de los lados del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Devuelve la representación en cadena legible del cuadrado.
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
