#!/usr/bin/python3
""" this module connect the database with python using argv
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


# modifying model_city
class City(Base):
    """ class to create table"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
