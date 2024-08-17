from sqlalchemy.orm import Session
from models.movie import Movie, MovieCategory
from schemas.movie import MovieCreate, MovieUpdate


def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(
        title=movie.title,
        description=movie.description,
        duration=movie.duration,
        release_date=movie.release_date,
        rating=movie.rating,
        image=movie.image,
        video=movie.video
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    for category_id in movie.categories:
        db_movie_category = MovieCategory(
            movie_id=db_movie.id, category_id=category_id)
        db.add(db_movie_category)
        db.commit()
        db.refresh(db_movie_category)

    return db_movie


def update_movie(db: Session, movie_id: int, movie: MovieUpdate):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie:
        for key, value in movie.dict(exclude_unset=True).items():
            setattr(db_movie, key, value)
        db.commit()
        db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie


def get_all_movies(db: Session):
    return db.query(Movie).all()


# def get_movies_with_categories(db: Session):
#     return db.query(Movie).join(Movie.categories).all()


def get_some_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Movie).offset(skip).limit(limit).all()
