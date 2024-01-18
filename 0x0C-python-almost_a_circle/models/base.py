#!/usr/bin/python3
"""module for the base class 
    """


class Base:
    """the base class
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """constrcutor

        Args:
            id (_type_, int): _takes id and assign it to the objecct_. Defaults to None.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
