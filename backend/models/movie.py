from database import Base
from sqlalchemy import Column, Integer, String


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year_released = Column(Integer)
    type = Column(String)
    genre = Column(String)
    associated_people = Column(String)
