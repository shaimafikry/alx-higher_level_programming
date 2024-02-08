#!/usr/bin/python3
"""module for the base class
    """


class Base:
    """the base class
    Args:
    __nb.objects: nm of obj
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constrcutor

        Args:
        id (int): _takes id and assign it to the objecct_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
