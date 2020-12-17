#!/usr/bin/python3
"""
MODEL_CITY MODULE

Provides the class and methods to interact with the cities table in the DB.
"""

from relationship_state import Base, State
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    """Represents a City in the DB"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement="auto",
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
