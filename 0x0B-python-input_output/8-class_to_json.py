#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def class_to_json(obj):
    """loop through __dict__ of a class

    Args:
        obj (_type_): class instance

    Returns:
        _type_: dictionary
    """
    attr = {k: v for k, v in obj.__dict__.items()}
    return attr
