#!/usr/bin/python3
""" class
    """


class BaseGeometry:
    """ class
    """

    def area(self):

        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):

        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
