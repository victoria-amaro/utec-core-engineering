#!/usr/bin/env python3
"""
Módulo que define la clase Square con un atributo de tamaño privado.
"""


class Square:
    """
    Representa un cuadrado con un tamaño determinado.
    """

    def __init__(self, size):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size: El tamaño del lado del cuadrado.
        """
        self.__size = size
