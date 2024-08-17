from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    showtime_id = Column(Integer, ForeignKey('showtimes.id'))
    seat_id = Column(Integer, ForeignKey('seats.id'))
    purchase_date = Column(DateTime)

    user = relationship("User", back_populates="tickets")
    showtime = relationship("Showtime", back_populates="tickets")
    seat = relationship("Seat", back_populates="tickets")
