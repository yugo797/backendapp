from pydantic import BaseModel


class SeatBase(BaseModel):
    theater_id: int
    seat_number: str
    seat_type: str


class SeatCreate(SeatBase):
    pass


class SeatUpdate(SeatBase):
    pass


class Seat(SeatBase):
    id: int

    class Config:
        from_attributes = True  

