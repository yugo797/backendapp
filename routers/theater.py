from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.theater import Theater, TheaterCreate, TheaterUpdate
from crud.theater import get_theater, create_theater, update_theater, delete_theater, get_all_theaters, get_theaters_by_location
from database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=Theater)
def create_new_theater(theater: TheaterCreate, db: Session = Depends(get_db)):
    return create_theater(db=db, theater=theater)


@router.get("/{theater_id}", response_model=Theater)
def read_theater(theater_id: int, db: Session = Depends(get_db)):
    db_theater = get_theater(db, theater_id)
    if db_theater is None:
        raise HTTPException(status_code=404, detail="Theater not found")
    return db_theater


@router.get("/{location_id}", response_model=Theater)
def read_theaters_by_location(location_id: int, db: Session = Depends(get_db)):
    db_theater = get_theaters_by_location(db, location_id)
    if db_theater is None:
        raise HTTPException(status_code=404, detail="Theater not found")
    return db_theater


@router.get("/", response_model=List[Theater])
def read_all_theaters(db: Session = Depends(get_db)):
    return get_all_theaters(db)


@router.put("/{theater_id}", response_model=Theater)
def update_existing_theater(theater_id: int, theater: TheaterUpdate, db: Session = Depends(get_db)):
    db_theater = update_theater(db=db, theater_id=theater_id, theater=theater)
    if db_theater is None:
        raise HTTPException(status_code=404, detail="theater not found")
    return db_theater


@router.delete("/{theater_id}", response_model=Theater)
def delete_existing_theater(theater_id: int, db: Session = Depends(get_db)):
    db_theater = delete_theater(db, theater_id)
    if db_theater is None:
        raise HTTPException(status_code=404, detail="theater not found")
    return db_theater
