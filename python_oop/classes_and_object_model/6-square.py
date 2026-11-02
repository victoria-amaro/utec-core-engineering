#!/usr/bin/env python3
"""
Módulo que define la clase Square con position y representación en cadena.
"""


class Square:
    """
    Representa un cuadrado con tamaño y posición.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del cuadrado. Por defecto 0.
            position (tuple): La posición (x, y) del cuadrado. Por defecto (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter para size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter para size con validaciones."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter para position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter para position con validaciones."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado usando # y tomando en cuenta la posición."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado."""
        res = []
        if self.__size == 0:
            return ""

        for _ in range(self.__position[1]):
            res.append("")

        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)
