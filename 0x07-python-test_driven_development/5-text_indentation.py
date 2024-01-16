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
    new_str = ""
    for i in text:
        new_str += i
        if i in [":", "?", "."]:
            print(new_str.strip())
            print()
            new_str = ""

    if new_str:
        print(new_str.strip(), end="")
