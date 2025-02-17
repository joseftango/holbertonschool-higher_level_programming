#!/usr/bin/python3
'''all State objects that contain the letter\
    a from the database hbtn_0e_6_usa'''
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
    my_objs = {obj.id: obj.name for obj in result if 'a' in obj.name}
    keys = list(my_objs.keys())
    keys.sort()
    sorted_objs = {k: my_objs[k] for k in keys}

    for id, name in sorted_objs.items():
        print('{}: {}'.format(id, name))

    session.close()
