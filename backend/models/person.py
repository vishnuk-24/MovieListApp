from database import Base
from sqlalchemy import Column, Integer, String


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    profession = Column(String)
    known_for_titles = Column(String)
