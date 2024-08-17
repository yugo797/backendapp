from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Showtime(Base):
    __tablename__ = 'showtimes'
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    movie = relationship("Movie", back_populates="showtimes")
    theater = relationship("Theater", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime")
