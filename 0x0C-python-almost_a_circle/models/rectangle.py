#!/usr/bin/python3
"""rectangle inherts from base
     """

from .base import Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


@property
def width(self):
    return self.__width


@width.setter
def width(self, value):
    self.__width = value


@property
def height(self):
    return self.__height


@height.setter
def height(self, value):
    self.__height = value


@property
def y(self):
    """Set/get the y coordinate of the Rectangle."""
    return self.__y


@y.setter
def y(self, value):
    self.__y = value


@property
def x(self):
    return self.__x

@x.setter
def x(self, value):
    self.__x = value
