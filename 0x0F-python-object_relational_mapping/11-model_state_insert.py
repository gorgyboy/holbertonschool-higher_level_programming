#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

model_state_insert module provides function to add an State object to the DB.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_insert():
    """
    Adds the State object “Louisiana” to the database.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    model_state_insert()
