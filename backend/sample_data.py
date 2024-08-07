import csv
from io import StringIO
import gzip

from sqlalchemy.orm import Session

from models.movie import Movie
from models.person import Person
from models.user import User
from database import SessionLocal, engine


def import_sample_person_data(db: Session):
    """Import sample person data into the database."""
    sample_data = """id\tname\tbirth_year\tprofession\tknown_for_titles
1\tJohn Doe\t1980\tActor\tMovie1, Movie2
2\tJane Smith\t1990\tDirector\tMovie3
"""
    f = StringIO(sample_data)
    reader = csv.reader(f, delimiter="\t")
    next(reader)  # Skip header
    for row in reader:
        person = Person(
            name=row[1],
            birth_year=int(row[2]) if row[2] != "\\N" else None,
            profession=row[3],
            known_for_titles=row[4],
        )
        db.add(person)
    db.commit()


def import_sample_movie_data(db: Session):
    """Import sample movie data into the database."""
    sample_data = """id\ttitle\tyear_released\ttype\tgenre
1\tMovie1\t2001\tFeature\tDrama
2\tMovie2\t2002\tFeature\tComedy
"""
    f = StringIO(sample_data)
    reader = csv.reader(f, delimiter="\t")
    next(reader)  # Skip header
    for row in reader:
        movie = Movie(
            title=row[1],
            year_released=int(row[2]) if row[2] != "\\N" else None,
            type=row[3],
            genre=row[4],
        )
        db.add(movie)
    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    import_sample_person_data(db)
    import_sample_movie_data(db)
    db.close()