#!/usr/bin/env python3


def uppercase(str):
    """Imprime una cadena en mayúsculas usando conversión ASCII."""
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
