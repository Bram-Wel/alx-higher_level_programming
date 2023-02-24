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
    query_state = session.query(State).order_by(State.id).first()
    if query_state:
        print(f"{query_state.id}: {query_state.name}")
    else:
        print("Nothing")
    session.close()
