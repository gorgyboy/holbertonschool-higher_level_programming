#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

model_state_filter_a module provides function to get that contain the letter
'a' from the states table in the DB.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


def model_state_filter_a():
    """
    Lists all State objects that contain the letter a from the database.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).filter(text("name LIKE BINARY '%a%'"))\
            .order_by(State.id.asc()):
        print('{}: {}'.format(row.id, row.name))

    session.close()


if __name__ == "__main__":
    model_state_filter_a()
