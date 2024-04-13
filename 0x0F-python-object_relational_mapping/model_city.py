#!/usr/bin/python3
"""
Contains the class definition of a city
"""
from model_state import Base
from sqlalchemy import Column, Interger, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    Class that Defines each city
    """
    __tablename__ = 'cities'
    id = Column(Interger, unique, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    State_id = Column(Interger, Foreignkey("States.id"), nullable=False)
