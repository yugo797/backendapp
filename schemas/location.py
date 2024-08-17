from pydantic import BaseModel


class LocationBase(BaseModel):
    city: str = "Podgorica"
    country: str = "Crna Gora"
    place: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    class Config:
        from_attributes = True  
