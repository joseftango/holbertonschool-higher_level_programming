#!/usr/bin/python3
'''prints the first State object from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    record = session.query(State).first()
    if record:
        print('{}: {}'.format(record.id, record.name))
    else:
        print('Nothing')

    session.close()
