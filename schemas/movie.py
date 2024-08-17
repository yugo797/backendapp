from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from .category import Category


class MovieBase(BaseModel):
    title: str
    description: str
    duration: int
    release_date: date
    rating: float
    image: str
    video: str


class MovieCreate(MovieBase):
    categories: List[int] = []


class MovieUpdate(MovieBase):
    title: str | None = None
    description: str | None = None


class Movie(MovieBase):
    id: int
    categories: List[Category] = []

    class Config:
        from_attributes = True  

