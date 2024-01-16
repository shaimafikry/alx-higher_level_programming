#!/usr/bin/python3
"""module for func text_identication
    """


def text_indentation(text):
    """
    function that prints a text with 2
    new lines after each of these characters:
    ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in [':', '?', '.']:
            print(i)
            print()
        else:
            print(i, end="")
