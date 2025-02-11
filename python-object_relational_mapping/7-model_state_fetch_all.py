#!/usr/bin/python3
'''fetch all states from the database "hbtn_0e_6_usa"'''
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
    result = session.query(State).all()
    records = {obj.id: obj.name for obj in result}
    keys = list(records.keys())
    keys.sort()
    sorted_records = {k: records[k] for k in keys}

    for k, v in sorted_records.items():
        print('{}: {}'.format(k, v))

    session.close()
