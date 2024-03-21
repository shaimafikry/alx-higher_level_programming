#!/usr/bin/python3
"""Start link class to table in database 
"""
from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """connection start => not really start before actually calling a query order"""
    """make connection to sql using user and password"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    """creates the tables based on class state defined at the other module"""
    Base = declarative_base()
    Base.metadata.create_all(engine)
    