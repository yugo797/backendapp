from pydantic import BaseModel
from typing import List
from .movie import Movie


class WishlistBase(BaseModel):
    user_id: int


class WishlistCreate(WishlistBase):
    movie_ids: List[int] = []


class WishlistUpdate(WishlistBase):
    movie_ids: List[int]


class Wishlist(WishlistBase):
    id: int
    movies: List[Movie] = []

    class Config:
        from_attributes = True
