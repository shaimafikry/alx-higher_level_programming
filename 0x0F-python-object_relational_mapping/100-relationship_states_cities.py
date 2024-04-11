#!/usr/bin/python3
"""add a state and a city related to with a relationship ()
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

# script that creates the State “California” with the City “San Francisco”
# from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    # creates all tables included, or obtain it from database
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = Session(engine)
    new_city = City(name='San Francisco', state=State(name='California'))
    session.add(new_city)
    session.commit()
