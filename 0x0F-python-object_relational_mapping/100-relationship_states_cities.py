#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

relationship_states_cities module provides function to create the
a State and City in the DB.
"""

import sys
from relationship_city import Base, City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


def relationship_states_cities():
    """
    Creates the State “California” with the City “San Francisco” in the
    database.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()

    session.close()


if __name__ == "__main__":
    relationship_states_cities()
