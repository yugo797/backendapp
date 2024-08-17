from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.showtime import Showtime, ShowtimeCreate, ShowtimeUpdate
from crud.showtime import get_showtime, create_showtime, get_showtimes_by_movie, get_all_showtimes, update_showtime, delete_showtime
from database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=Showtime)
def create_new_showtime(showtime: ShowtimeCreate, db: Session = Depends(get_db)):
    return create_showtime(db=db, showtime=showtime)


@router.get("/{showtime_id}", response_model=Showtime)
def read_showtime(showtime_id: int, db: Session = Depends(get_db)):
    db_showtime = get_showtime(db, showtime_id)
    if db_showtime is None:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return db_showtime


@router.get("/{movie_id}", response_model=Showtime)
def read_showtime_by_movie(movie_id: int, db: Session = Depends(get_db)):
    db_showtime = get_showtimes_by_movie(db, movie_id)
    if db_showtime is None:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return db_showtime


@router.get("/", response_model=List[Showtime])
def read_all_showtimes(db: Session = Depends(get_db)):
    return get_all_showtimes(db)


@router.put("/{showtime_id}", response_model=Showtime)
def update_existing_showtime(showtime_id: int, showtime: ShowtimeUpdate, db: Session = Depends(get_db)):
    db_showtime = update_showtime(
        db=db, showtime_id=showtime_id, showtime=showtime)
    if db_showtime is None:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return db_showtime


@router.delete("/{showtime_id}", response_model=Showtime)
def delete_existing_showtime(showtime_id: int, db: Session = Depends(get_db)):
    db_showtime = delete_showtime(db, showtime_id)
    if db_showtime is None:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return db_showtime
