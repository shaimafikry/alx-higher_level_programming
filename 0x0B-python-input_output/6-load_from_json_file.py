#!/usr/bin/python3
"""module for  Python - Input/Output
    """
import json


def load_from_json_file(filename):
    """convert from json to string

    Args:
        my_obj (string): to be converted
        filename: to put into
    """
    with open(filename, "r", encoding="utf-8") as f_new:
        return json.load(f_new)
