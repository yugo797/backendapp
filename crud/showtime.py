from sqlalchemy.orm import Session
from models.showtime import Showtime
from schemas.showtime import ShowtimeCreate


def get_showtime(db: Session, showtime_id: int):
    return db.query(Showtime).filter(Showtime.id == showtime_id).first()


def get_showtimes_by_movie(db: Session, movie_id: int):
    return db.query(Showtime).filter(Showtime.movie_id == movie_id).all()


def create_showtime(db: Session, showtime: ShowtimeCreate):
    db_showtime = Showtime(**showtime.dict())
    db.add(db_showtime)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime


def update_showtime(db: Session, showtime_id: int, showtime: ShowtimeCreate):
    db_showtime = db.query(Showtime).filter(Showtime.id == showtime_id).first()
    if db_showtime:
        for key, value in showtime.dict(exclude_unset=True).items():
            setattr(db_showtime, key, value)
        db.commit()
        db.refresh(db_showtime)
    return db_showtime


def delete_showtime(db: Session, showtime_id: int):
    db_showtime = db.query(Showtime).filter(Showtime.id == showtime_id).first()
    if db_showtime:
        db.delete(db_showtime)
        db.commit()
    return db_showtime


def get_all_showtimes(db: Session):
    return db.query(Showtime).all()
