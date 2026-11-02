#!/usr/bin/env python3
"""
Módulo que define la clase BaseGeometry.
"""


class BaseGeometry:
    """
    Clase base para figuras geométricas.
    """

    def area(self):
        """
        Lanza una excepción indicando que el área no está implementada.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida que un valor sea un entero positivo mayor que 0.

        Args:
            name (str): Nombre de la variable a validar.
            value (int): Valor a validar.

        Raises:
            TypeError: Si el valor no es de tipo entero.
            ValueError: Si el valor es menor o igual a 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
