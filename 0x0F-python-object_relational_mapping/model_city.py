#!/usr/bin/python3
""" this module connect the database with python using argv
"""

import sqlalchemy as db
from sqlalchemy.orm import declarative_base


Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)

