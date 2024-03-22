#!/usr/bin/python3
""" this module connect the database with python using argv
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """ class to create the first table"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    # Define the relationship to City
    # Use backref to automatically create a 'state' attribute in the City class

cities = relationship("City",backref=backref('state',cascade="all, delete-orphan"))
