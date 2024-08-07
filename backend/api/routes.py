from datetime import timedelta

from auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    authenticate_user,
    create_access_token,
    create_user,
)
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.movie import Movie
from models.person import Person
from models.user import User
from schemas.movie import MovieSearch
from schemas.person import PersonSearch
from schemas.user import UserCreate

router = APIRouter()


@router.get("/", response_model=dict)
async def read_root():
    return {"Hello": "World"}


@router.post("/register", response_model=dict)
async def register_user(user: UserCreate, db=Depends(get_db)):
    db_user = create_user(db, user.username, user.password)
    return {"message": "User created successfully"}


@router.post("/token", response_model=dict)
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


@router.post("/search_movie")
async def search_movie(search: MovieSearch, db=Depends(get_db)):
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
            "associated_people": m.associated_people.split(",") if m.associated_people else None,
        }
        for m in movies
    ]


@router.post("/search_person")
async def search_person(search: PersonSearch, db=Depends(get_db)):
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
            "known_for_titles": p.known_for_titles.split(",") if p.known_for_titles else None,
        }
        for p in persons
    ]
