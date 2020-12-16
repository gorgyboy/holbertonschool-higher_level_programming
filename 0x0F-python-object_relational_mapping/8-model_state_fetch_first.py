#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

Model_State_Fetch_First module provides function to get the first state from
states table in the DB.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_first():
    """
    Prints the first State object from the database.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).first()
    if row is None:
        print('Nothing')
    else:
        print('{}: {}'.format(row.id, row.name))

    session.close()


if __name__ == "__main__":
    model_state_fetch_first()
