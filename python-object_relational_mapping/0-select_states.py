#!/usr/bin/python3
'''0-select_states module'''
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


username = argv[1]
password = argv[2]
database = argv[3]

DATABASE_URL = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()

for state in states:
    print(f'({state.id}, {state.name})')

session.close()
