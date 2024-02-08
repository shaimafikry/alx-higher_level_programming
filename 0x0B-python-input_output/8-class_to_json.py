#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def class_to_json(obj):
    attr = {k: v for k, v in obj.__dict__.items()}
    return attr
