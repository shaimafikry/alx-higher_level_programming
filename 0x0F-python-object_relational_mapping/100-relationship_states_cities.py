#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from model_city import City, Base


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = Session(engine)
    cities = session.query(City, State).filter(City.state_id == State.id)
    for city, state in cities:
        print(("{}: ({}) {}").format(state.name, city.id, city.name))
    session.close()





State class:
In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state

Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
You must use the cities relationship for all State objects
Your code should not be executed when imported
