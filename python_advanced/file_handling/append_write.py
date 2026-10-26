#!/usr/bin/env python3
"""
Modulo para agregar contenido a un archivo de texto.
"""


def append_write(filename="", text=""):
    """Agrega una cadena al final de un archivo UTF-8."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
