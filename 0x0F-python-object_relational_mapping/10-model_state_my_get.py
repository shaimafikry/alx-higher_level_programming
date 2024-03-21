#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    # select * from states where name like '%a%' order by states.id
    state = session.query(State).filter(State.name==(sys.argv[4]))
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Not found")
        
    session.close()
