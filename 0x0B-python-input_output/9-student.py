#!/usr/bin/python3
"""module for  class student
    """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        dic = {k: v for k, v in self.__dict__.items()}
        return dic
