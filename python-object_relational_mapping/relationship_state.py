#!/usr/bin/python3
'''State_relationship module'''
from sqlalchemy.orm import relationship
from model_city import Base
from model_state import State


State.cities = relationship('City',
                            back_populates="state", cascade="all, delete")
