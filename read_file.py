#!/usr/bin/env python3
"""
Modulo para lectura de archivos de texto.
"""


def read_file(filename=""):
    """Lee un archivo UTF-8 e imprime su contenido en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
