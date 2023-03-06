#!/usr/bin/python3
"""Create the State of California and San Francisco city in the state."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from relationship_city import State, Base, City


def printer(state):
    """Print the state & cities in state."""
    print(f"{state.id}: {state.name}")
    for city in state.cities:
        print(f"\t{city.id}: {city.name}")


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}')
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        printer(state)
    session.close()
