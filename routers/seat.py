from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.seat import Seat, SeatCreate, SeatUpdate
from crud.seat import get_seat, create_seat, get_seats_by_theater, get_all_seats, update_seat, delete_seat
from database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=Seat)
def create_new_seat(seat: SeatCreate, db: Session = Depends(get_db)):
    return create_seat(db=db, seat=seat)


@router.get("/{seat_id}", response_model=Seat)
def read_seat(seat_id: int, db: Session = Depends(get_db)):
    db_seat = get_seat(db, seat_id)
    if db_seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")
    return db_seat


@router.get("/{theater_id}", response_model=Seat)
def read_seat_by_theater(theater_id: int, db: Session = Depends(get_db)):
    db_seat = get_seats_by_theater(db, theater_id)
    if db_seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")
    return db_seat


@router.get("/", response_model=List[Seat])
def read_all_seats(db: Session = Depends(get_db)):
    return get_all_seats(db)


@router.put("/{seat_id}", response_model=Seat)
def update_existing_seat(seat_id: int, seat: SeatUpdate, db: Session = Depends(get_db)):
    db_seat = update_seat(db=db, seat_id=seat_id, seat=seat)
    if db_seat is None:
        raise HTTPException(status_code=404, detail="seat not found")
    return db_seat


@router.delete("/{seat_id}", response_model=Seat)
def delete_existing_seat(seat_id: int, db: Session = Depends(get_db)):
    db_seat = delete_seat(db, seat_id)
    if db_seat is None:
        raise HTTPException(status_code=404, detail="seat not found")
    return db_seat
