#!/usr/bin/python3
"""module for  Python - Input/Output
    """
import json


def to_json_string(my_obj):
    """conver string to json

    Args:
        my_obj (string):
    Returns:
        json represintation
    """
    return json.dumps(my_obj)
