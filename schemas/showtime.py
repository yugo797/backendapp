from pydantic import BaseModel
from datetime import datetime


class ShowtimeBase(BaseModel):
    movie_id: int
    theater_id: int
    start_time: datetime
    end_time: datetime


class ShowtimeCreate(ShowtimeBase):
    pass


class ShowtimeUpdate(ShowtimeBase):
    pass


class Showtime(ShowtimeBase):
    id: int

    class Config:
        from_attributes = True  
