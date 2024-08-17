from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(500), index=True)
    duration = Column(Integer)
    release_date = Column(Date)
    rating = Column(Float)
    image = Column(String(500), index=True)
    video = Column(String(500), index=True)
    # category = Column(String(25))

    categories = relationship(
        "Category", secondary="movie_categories", back_populates="movies")
    showtimes = relationship("Showtime", back_populates="movie")
    wishlists = relationship(
        "Wishlist", secondary='wishlist_movie', back_populates="movies")


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16), index=True)

    movies = relationship(
        "Movie", secondary="movie_categories", back_populates="categories")


class MovieCategory(Base):
    __tablename__ = 'movie_categories'
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey(
        'categories.id'), primary_key=True)
