#!/usr/bin/python3
"""is instance func
    """


def is_same_class(obj, a_class):
    """check if the object is instance
        return true or false
    Args:
        obj (instance): ogj checked
        a_class (_type_): class check
    """

    if type(obj) is a_class:
        return True
    return False
