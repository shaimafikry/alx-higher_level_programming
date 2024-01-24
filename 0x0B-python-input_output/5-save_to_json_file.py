#!/usr/bin/python3
"""module for  Python - Input/Output
    """
import json


def save_to_json_file(my_obj, filename):
    """convert string to json in a file

    Args:
        my_obj (string): to be converted
        filename: to put into
    """
    with open(filename, "w", encoding="utf-8") as f_new:
        json.dump(my_obj, f_new)
