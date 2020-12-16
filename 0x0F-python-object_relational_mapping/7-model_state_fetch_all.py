#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

Model_State_Fetch_All module provides function to get all states from states
table in the DB.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_state_fetch_all():
    """
    Lists all State objects from the database and show results sorted in
    ascending order by states.id.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id.asc()):
        print('{}: {}'.format(row.id, row.name))

    session.close()


if __name__ == "__main__":
    model_state_fetch_all()
