from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./movie_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Models
class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    profession = Column(String)
    known_for_titles = Column(String)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year_released = Column(Integer)
    type = Column(String)
    genre = Column(String)
    associated_people = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


Base.metadata.create_all(bind=engine)


# Pydantic models
class MovieSearch(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
    person_name: Optional[str] = None
    type: Optional[str] = None


class PersonSearch(BaseModel):
    name: Optional[str] = None
    movie_title: Optional[str] = None
    profession: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: str
    password: str


# JWT settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Authentication functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_user(db: Depends(get_db), username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already registered")


# API endpoints
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register", response_model=dict)
async def register_user(user: UserCreate, db=Depends(get_db)):
    db_user = create_user(db, user.username, user.password)
    return {"message": "User created successfully"}


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/search_movie")
async def search_movie(
    search: MovieSearch, db=Depends(get_db), token: str = Depends(oauth2_scheme)
):
    # Implement movie search logic here
    query = db.query(Movie)
    if search.title:
        query = query.filter(Movie.title.ilike(f"%{search.title}%"))
    if search.year:
        query = query.filter(Movie.year_released == search.year)
    if search.genre:
        query = query.filter(Movie.genre.ilike(f"%{search.genre}%"))
    if search.type:
        query = query.filter(Movie.type == search.type)
    if search.person_name:
        query = query.filter(Movie.associated_people.ilike(f"%{search.person_name}%"))

    movies = query.all()
    return [
        {
            "title": m.title,
            "year_released": m.year_released,
            "type": m.type,
            "genre": m.genre,
            "associated_people": m.associated_people.split(","),
        }
        for m in movies
    ]


@app.post("/search_person")
async def search_person(
    search: PersonSearch, db=Depends(get_db), token: str = Depends(oauth2_scheme)
):
    # Implement person search logic here
    query = db.query(Person)
    if search.name:
        query = query.filter(Person.name.ilike(f"%{search.name}%"))
    if search.profession:
        query = query.filter(Person.profession.ilike(f"%{search.profession}%"))
    if search.movie_title:
        query = query.filter(Person.known_for_titles.ilike(f"%{search.movie_title}%"))

    persons = query.all()
    return [
        {
            "name": p.name,
            "birth_year": p.birth_year,
            "profession": p.profession,
            "known_for_titles": p.known_for_titles.split(","),
        }
        for p in persons
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
