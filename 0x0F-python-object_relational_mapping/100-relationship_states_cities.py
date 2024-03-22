#!/usr/bin/python3
"""add a state and a city related to with a relationship ()
"""

import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker



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
    new_state = State(name='California',id=1)
    session.add(new_state)
    session.commit()
    new_city = City(name='San Francisco', state_id=new_state.id)
    session.add(new_city)
    session.commit()
    
    session.close()
