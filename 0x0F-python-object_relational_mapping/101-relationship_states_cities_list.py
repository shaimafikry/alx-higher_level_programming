#!/usr/bin/python3
"""model to list all states and cities related to in a specific format
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    # make connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # creates all table or retrive the data from db
    Base.metadata.create_all(engine)
    # starting my session
    session = Session(engine)
    # get all states with related city (power of relationship)
    data = session.query(State).order_by(State.id).all()
    i = 0
    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            i += 1
            print('\t', "{}: {}".format(i, city.name))
    # ends my connection
    session.close()
