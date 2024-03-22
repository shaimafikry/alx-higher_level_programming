#!/usr/bin/python3
"""add a state and a city related to with a relationship ()
"""

import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City


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
    new_state = session.add(State(name='California', id=1))
    new_city = session.add(City(name='San Francisco', id=1))
    session.commit()
    session.close()
