#!/usr/bin/python3
"""List all State objects from a the database."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}', pool_pre_ping=True)
    # Base.metadata.create_all(engine)

    session = Session(engine)
    query_state = session.query(State).filter(State.id == 2).first()
    query_state.name = "New Mexico"
    session.commit()
    session.close()
