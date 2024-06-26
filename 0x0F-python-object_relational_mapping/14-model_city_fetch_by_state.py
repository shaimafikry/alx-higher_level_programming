#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from model_city import City, Base

# Python file similar to model_state.py named model_city.py
# that contains the class definition of a City
if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(City, State).filter(City.state_id == State.id)
    for city, state in cities:
        print(("{}: ({}) {}").format(state.name, city.id, city.name))
    session.close()
