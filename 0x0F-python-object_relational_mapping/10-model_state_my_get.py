#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

model_state_my_get module provides function to prints the State object with the
name passed as argument from the DB.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, text, String
from sqlalchemy.orm import sessionmaker


def model_state_my_get():
    """
    Prints the State object with the name passed as argument from the database.

    Takes 4 arguments: mysql username, mysql password, database name and
    state name to search (SQL injection free).
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State.id).filter(
        text("name LIKE BINARY :name").bindparams(name=sys.argv[4])).first()
    if row is None:
        print('Not found')
    else:
        print(row.id)

    session.close()


if __name__ == "__main__":
    model_state_my_get()
