#!/usr/bin/python3
"""Create the State of California and San Francisco city in the state."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from relationship_city import State, Base, City


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}')
    Base.metadata.create_all(engine)

    session = Session(engine)
    for id, city, state in session.query(City.id, City.name, State.name).join(
            State).order_by(City.id).all():
        print(f"{id}: {city} -> {state}")
    session.close()
