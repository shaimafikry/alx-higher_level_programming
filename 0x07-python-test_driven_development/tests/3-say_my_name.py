#!/usr/bin/python3
"""modle for say my name
    """


def say_my_name(first_name, last_name=""):
    """prints my name

    Args:
        first_name (str): first nme
        last_name (str, optional): sec nmae , defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
