#!/usr/bin/python3
"""Print all City objects from DB hbtn_0e_14_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/\
{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city in session.query(City).join(State).order_by(City.id).all():
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()
