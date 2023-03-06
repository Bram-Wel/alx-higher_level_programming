#!/usr/bin/python3
"""A State Class that inherits from SQLAlchemy's Base class"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    """Mapped State Class.

    Args:
        @Base (Base): The declarative base class maintaining a catalogue of all
        classes & tables relative to it
    Attributes:
        tablename (str): Name of table in the database
        id (int): Unique identifier for the state
        name (str): Name of the state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade="all, delete-orphan")
