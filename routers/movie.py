from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.movie import Movie, MovieCreate, MovieUpdate
from crud.movie import get_movie, create_movie, get_some_movies, get_all_movies, delete_movie, update_movie
from database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=Movie)
def create_new_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db=db, movie=movie)


@router.get("/{movie_id}", response_model=Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.get("/", response_model=List[Movie])
def read_some_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_some_movies(db, skip=skip, limit=limit)


@router.get("/", response_model=List[Movie])
def read_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)


@router.put("/{movie_id}", response_model=Movie)
def update_existing_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    db_movie = update_movie(db=db, movie_id=movie_id, movie=movie)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.delete("/{movie_id}", response_model=Movie)
def delete_existing_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = delete_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie
