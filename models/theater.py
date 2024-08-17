# from sqlalchemy import Column, Integer, String, ForeignKey
# from ..database import Base


# class Theater(Base):
#     __tablename__ = "theaters"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     location_id = Column(Integer, ForeignKey("locations.id"))

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Theater(Base):
    __tablename__ = 'theaters'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(26), index=True)
    location_id = Column(Integer, ForeignKey('locations.id'))

    location = relationship("Location", back_populates="theaters")
    showtimes = relationship("Showtime", back_populates="theater")
    seats = relationship("Seat", back_populates="theater")


class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(30), index=True)
    place = Column(String(200), index=True)
    country = Column(String(30), index=True)

    theaters = relationship("Theater", back_populates="location")
