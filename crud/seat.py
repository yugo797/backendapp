from sqlalchemy.orm import Session
from models.seat import Seat
from schemas.seat import SeatCreate


def get_seat(db: Session, seat_id: int):
    return db.query(Seat).filter(Seat.id == seat_id).first()


def get_seats_by_theater(db: Session, theater_id: int):
    return db.query(Seat).filter(Seat.theater_id == theater_id).all()


def create_seat(db: Session, seat: SeatCreate):
    db_seat = Seat(**seat.dict())
    db.add(db_seat)
    db.commit()
    db.refresh(db_seat)
    return db_seat


def update_seat(db: Session, seat_id: int, seat: SeatCreate):
    db_seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if db_seat:
        for key, value in seat.dict(exclude_unset=True).items():
            setattr(db_seat, key, value)
        db.commit()
        db.refresh(db_seat)
    return db_seat


def delete_seat(db: Session, seat_id: int):
    db_seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if db_seat:
        db.delete(db_seat)
        db.commit()
    return db_seat


def get_all_seats(db: Session):
    return db.query(Seat).all()
