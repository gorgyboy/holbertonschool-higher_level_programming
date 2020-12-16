#!/usr/bin/python3
"""
PYTHON OBJECT RELATIONAL MAPPING MODULE

model_city_fetch_by_state module provides function to get all cities from
cities table in the DB.
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_city_fetch_by_state():
    """
    Prints all City objects from the database and show results sorted in
    ascending order by cities.id.

    Takes 3 arguments: mysql username, mysql password and database name.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id.asc()).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    model_city_fetch_by_state()
