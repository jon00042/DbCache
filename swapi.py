from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func
from base import Base, inverse_relationship, create_tables

class Film(Base):
    __tablename__ = 'swapi_films'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    title = Column(String)
    episode_id = Column(Integer)
    opening_crawl = Column(String)
    director = Column(String)
    producer = Column(String)
    release_date = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Person(Base):
    __tablename__ = 'swapi_people'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    name = Column(String)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Planet(Base):
    __tablename__ = 'swapi_planets'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    name = Column(String)
    rotation_period = Column(String)
    orbital_period = Column(String)
    diameter = Column(String)
    climate = Column(String)
    gravity = Column(String)
    terrain = Column(String)
    surface_water = Column(String)
    population = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Species(Base):
    __tablename__ = 'swapi_species'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    skin_colors = Column(String)
    hair_colors = Column(String)
    eye_colors = Column(String)
    average_lifespan = Column(String)
    language = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Starship(Base):
    __tablename__ = 'swapi_starships'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    max_atmosphering_speed = Column(String)
    crew = Column(String)
    passengers = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    hyperdrive_rating = Column(String)
    MGLT = Column(String)
    starship_class = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Vehicle(Base):
    __tablename__ = 'swapi_vehicles'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    max_atmosphering_speed = Column(String)
    crew = Column(String)
    passengers = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    vehicle_class = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



