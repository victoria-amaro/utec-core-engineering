#!/usr/bin/env python3


def pow(a, b):
    """Devuelve a elevado a la potencia b."""
    if b == 0:
        return 1

    exp = abs(b)
    result = 1
    for _ in range(exp):
        result *= a

    if b < 0:
        return 1 / result
    return result
