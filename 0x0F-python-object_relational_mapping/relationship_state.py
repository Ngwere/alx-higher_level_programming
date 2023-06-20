#!/usr/bin/python3
"""
Define the city class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representation of a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
