from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


class WishlistMovie(Base):
    __tablename__ = 'wishlist_movie'
    wishlist_id = Column(Integer, ForeignKey('wishlists.id'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)


class Wishlist(Base):
    __tablename__ = 'wishlists'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="wishlist")
    movies = relationship(
        "Movie", secondary="wishlist_movie", back_populates="wishlists")
