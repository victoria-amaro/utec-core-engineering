#!/usr/bin/env python3
"""
Módulo que define la clase Square con getter y setter para size.
"""


class Square:
    """
    Representa un cuadrado con un tamaño determinado.
    """

    def __init__(self, size=0):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado. Por defecto 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter para obtener el tamaño del cuadrado.

        Returns:
            int: El tamaño actual del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter para actualizar el tamaño del cuadrado con validación.

        Args:
            value (int): El nuevo tamaño.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado (size * size).
        """
        return self.__size ** 2
