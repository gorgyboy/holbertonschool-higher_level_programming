#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

model_state_delete_a module provides function to delete all State objects
with a name containing the letter a from the DB.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


def model_state_delete_a():
    """
    Deletes all State objects with a name containing the letter a from the
    database.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(text("name LIKE BINARY '%a%'")
                                ).delete(synchronize_session=False)
    session.commit()

    session.close()


if __name__ == "__main__":
    model_state_delete_a()
