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


def get_width(self):
    """width getter
    """
    return self.__width


def set_width(self, width):
    """width setter
    """
    self.__width = width


@property
def height(self):
    return self.__height


@height.setter
def height(self, value):
    self.__height = value


@property
def y(self):
    return self.__y


@y.setter
def y(self, value):
    self.__y = value


def get_x(self):
    """x getter
    """
    return self.__x


def set_x(self, x):
    """ x setter
    """
    self.__x = x
