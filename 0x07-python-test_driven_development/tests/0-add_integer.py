#!/usr/bin/python3
"""
    this module contains add function
    """


def add_integer(a, b=98):
    """function to add two integers

    Args:
        a (int): 
        b (int, optional):  Defaults to 98.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
