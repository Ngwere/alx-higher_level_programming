#!/usr/bin/python3
"""
Lists all state objects from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
 
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    newstate = State(name = 'California')
    newstate.cities.append(City(name='San Francisco'))
    session.add(newstate)
    session.commit()
    session.close()
