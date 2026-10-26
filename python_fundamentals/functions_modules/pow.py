#!/usr/bin/env python3


def pow(a, b):
    """Devuelve a elevado a la potencia b."""
    if b < 0:
        return None
    result = 1
    for _ in range(b):
        result *= a
    return result
