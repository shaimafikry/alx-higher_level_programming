#!/usr/bin/python3
"""rectangle inherts from base
    """


from .rectangle import Rectangle


class Square(Rectangle):
    """class square iherts from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assign values to attr"""
        if not args:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            attrs = ("id", "size", "x", "y")
            for a, i in zip(attrs, args):
                setattr(self, a, i)

    def to_dictionary(self):
        """returns dict of attribute"""
        dic = {"id": "", "size": "", "x": "", "y": ""}
        for k in dic:
            dic[k] = getattr(self, k)
        return dic
