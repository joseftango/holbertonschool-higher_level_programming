#!/usr/bin/python3
'''City_relationship module'''
from sqlalchemy.orm import relationship
from model_city import City
from relationship_state import Base


City.state = relationship('State', back_populates="cities")
