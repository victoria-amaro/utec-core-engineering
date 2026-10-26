#!/usr/bin/env python3


def element_at(my_list, idx):
    """Devuelve el elemento en idx o None."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
