#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

# script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    session.add(State(name="Louisiana"))
    session.commit()
    # select state.id from states where name = 'Louisiana'
    state = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(state.id))
    session.close()
