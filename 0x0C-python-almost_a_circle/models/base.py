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
        lst_dict = []
        if list_objs is None:
            lst_dict = []
        else:
            for i in list_objs:
                lst_dict.append(i.to_dictionary())
        list_objs_dict = cls.to_json_string(lst_dict)
        filename = str(cls.__name__) + ".json"
        with open(filename, "w", encoding="utf-8") as fe:
            fe.write(list_objs_dict)

    @staticmethod
    def from_json_string(json_string):
        "reload from json string"
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribue set"""
        dummy = cls(1, 1, 1, 1, 1)
        return dummy.update(**dictionary)
