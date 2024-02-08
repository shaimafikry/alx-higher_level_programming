#!/usr/bin/python3
"""module for  class student
    """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs != None:
            if isinstance(attrs, list) and not attrs:
                return {}
            else:
                dic = {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            dic = {k: v for k, v in self.__dict__.items()}
        return dic
