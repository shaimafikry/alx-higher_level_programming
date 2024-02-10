#!/usr/bin/python3
"""module for the base class
    """


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json represntion of list dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save data o file"""
        """turns list of objects to dictionaries"""
        list_objs_dict = cls.to_json_string(list_objs)
        filename = cls.__name__+".json"
        with open(filename, "w", encoding="utf-8") as fe:
            fe.write(list_objs_dict)
