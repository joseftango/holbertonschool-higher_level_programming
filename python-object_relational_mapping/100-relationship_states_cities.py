#!/usr/bin/python3
'''prints all City objects from the database hbtn_0e_14_usa'''
import sys
from relationship_city import Base, City
from relationship_state import State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco', state=state)

    session.add(state)

    session.commit()
    session.close()
