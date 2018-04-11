from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func
from base import Base, inverse_relationship, create_tables

class City(Base):
    __tablename__ = 'dck_cities'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    state = Column(String)
    zipcode = Column(String)
    is_capital = Column(Integer)
    population = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Club(Base):
    __tablename__ = 'dck_clubs'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    league = Column(String)
    city = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Company(Base):
    __tablename__ = 'dck_companies'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    founded_on = Column(String)
    total_assets = Column(Float)
    revenue = Column(Float)
    operating_income = Column(Float)
    net_income = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Department(Base):
    __tablename__ = 'dck_departments'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    company = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Exchange(Base):
    __tablename__ = 'dck_exchanges'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    address = Column(String)
    city = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class League(Base):
    __tablename__ = 'dck_leagues'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    sport = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Person(Base):
    __tablename__ = 'dck_people'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    first = Column(String)
    last = Column(String)
    gender = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class State(Base):
    __tablename__ = 'dck_states'
    uniq_id = Column(Integer, primary_key=True)
    api = Column(String, unique=True)
    id = Column(Integer)
    name = Column(String)
    abbreviation = Column(String)
    gdp = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

