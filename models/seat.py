from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Seat(Base):
    __tablename__ = 'seats'
    id = Column(Integer, primary_key=True, index=True)
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    seat_number = Column(String(16), index=True)
    seat_type = Column(String(16))

    theater = relationship("Theater", back_populates="seats")
    tickets = relationship("Ticket", back_populates="seat")
