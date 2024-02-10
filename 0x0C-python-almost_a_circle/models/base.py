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
        """turns list of objects to dictionaries and save them to file"""
        lst_dict = []
        if list_objs is None:
            lst_dict = []
        else:
            for i in list_objs:
                """to_dictionary is a method on class in the list
                i represent an instance
                """
                lst_dict.append(i.to_dictionary())
        list_objs_dict = cls.to_json_string(lst_dict)
        filename = str(cls.__name__) + ".json"
        with open(filename, "w", encoding="utf-8") as fe:
            fe.write(list_objs_dict)

    @staticmethod
    def from_json_string(json_string):
        """reload from json string
        returns list of dictionaries"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribue set"""
        dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances with all attribue set"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as fe:
                """ inst hold list of dictionaries"""
                inst_dict = cls.from_json_string(fe.read())
                """list_inst hold list of instances after create"""
                inst_list = []
                for i in inst_dict:
                    inst_list.append(cls.create(**i))
                return inst_list
        except FileNotFoundError:
            return []
