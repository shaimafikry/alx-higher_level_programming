#!/usr/bin/python3
""" this module connect the database with python using argv
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#  python file that contains the class definition of a
# State and an instance Base = declarative_base()
Base = declarative_base()


class State(Base):
    """ class to create the first table"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
