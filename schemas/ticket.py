from pydantic import BaseModel
from datetime import datetime


class TicketBase(BaseModel):
    user_id: int
    showtime_id: int
    seat_id: int
    purchase_date: datetime


class TicketCreate(TicketBase):
    pass


class TicketUpdate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int

    class Config:
        from_attributes = True  
