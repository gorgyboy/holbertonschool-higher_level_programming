#!/usr/bin/python3
"""
MODEL_STATE MODULE

Provides the class and methods to interact with the states table in the DB.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a State in the DB"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement="auto",
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
