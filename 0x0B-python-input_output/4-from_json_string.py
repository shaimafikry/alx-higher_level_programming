#!/usr/bin/python3
"""module for  Python - Input/Output
    """
import json


def from_json_string(my_str):
    """convert from json to string

    Args:
        my_str (string):
    """
    return json.loads(my_str)
