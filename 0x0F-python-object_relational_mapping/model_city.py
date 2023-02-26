#!/usr/bin/python3
"""A City Class that inherits from SQLAlchemy's Base class"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from model_state import State, Base


class City(Base):
    """Mapped City Class.

    Args:
        @Base (Base): The declarative base class maintaining a catalogue of all
        classes & tables relative to it
    Attributes:
        tablename (str): Name of table in the database
        id (int): Unique identifier for the state
        name (str): Name of the state
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship('State', backref='City')
