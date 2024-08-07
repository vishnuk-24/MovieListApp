import csv
import gzip

from sqlalchemy.orm import Session

from main import Movie, Person, SessionLocal, engine


def import_person_data(file_path: str, db: Session):
    """
    Import person data from a gzip-compressed TSV file into the database.
    """
    with gzip.open(file_path, "rt") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)  # Skip header
        for row in reader:
            person = Person(
                name=row[1],
                birth_year=int(row[2]) if row[2] != "\\N" else None,
                profession=row[4],
                known_for_titles=row[5],
            )
            db.add(person)
    db.commit()


def import_movie_data(file_path: str, db: Session):
    """Import movie data from a gzip-compressed TSV file into the database."""
    with gzip.open(file_path, "rt") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)  # Skip header
        for row in reader:
            movie = Movie(
                title=row[2],
                year_released=int(row[5]) if row[5] != "\\N" else None,
                type=row[1],
                genre=row[8],
            )
            db.add(movie)
    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    import_person_data("/home/vishnu/Downloads/name.basics.tsv.gz", db)
    import_movie_data("/home/vishnu/Downloads/title.basics.tsv.gz", db)
    db.close()
