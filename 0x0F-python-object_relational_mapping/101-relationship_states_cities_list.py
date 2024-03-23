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
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],argv[2],argv[3]),pool_pre_ping=True)
    # creates all table or retrive the data from db
    Base.metadata.create_all(engine)
    # starting my session incase imma gonna add soething
    session = sessionmaker(bind=engine)
    session = Session(engine)
    data = session.query(City, State).filter(City.state_id==State.id).order_by(City.id, State.id)
    print (data)
    for state in data:
        print(state.id,state.name,':')
        for city in data:
            print ('\t',city.id,':',city.name)
        
    # ends my connection
    session.close()
