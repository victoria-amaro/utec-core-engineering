#!/usr/bin/env python3
"""
Modulo para escritura de archivos de texto.
"""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo UTF-8 y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
