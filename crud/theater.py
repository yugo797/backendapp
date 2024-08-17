from sqlalchemy.orm import Session
from models.theater import Theater
from schemas.theater import TheaterCreate


def get_theater(db: Session, theater_id: int):
    return db.query(Theater).filter(Theater.id == theater_id).first()


def get_theaters_by_location(db: Session, location_id: int):
    return db.query(Theater).filter(Theater.location_id == location_id).all()


def create_theater(db: Session, theater: TheaterCreate):
    db_theater = Theater(**theater.dict())
    db.add(db_theater)
    db.commit()
    db.refresh(db_theater)
    return db_theater


def update_theater(db: Session, theater_id: int, theater: TheaterCreate):
    db_theater = db.query(Theater).filter(Theater.id == theater_id).first()
    if db_theater:
        for key, value in theater.dict(exclude_unset=True).items():
            setattr(db_theater, key, value)
        db.commit()
        db.refresh(db_theater)
    return db_theater


def delete_theater(db: Session, theater_id: int):
    db_theater = db.query(Theater).filter(Theater.id == theater_id).first()
    if db_theater:
        db.delete(db_theater)
        db.commit()
    return db_theater


def get_all_theaters(db: Session):
    return db.query(Theater).all()
