#!/usr/bin/python3
"""
MODEL_CITY MODULE

Provides the class and methods to interact with the cities table in the DB.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Represents a City in the DB"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement="auto",
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
