#!/usr/bin/python3
"""is instance func
    """


def is_kind_of_class(obj, a_class):
    """check if the object is instance
        return true or false
    Args:
        obj (instance): ogj checked
        a_class (_type_): class check
    """

    if isinstance(obj, a_class):
        return True
    return False
