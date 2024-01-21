#!/usr/bin/python3
"""
module for look up
"""


def lookup(obj):
    """to look for atrrib and meth of an object

    Args:
        obj (any time)
    """

    n_list = dir(obj)
    return n_list
