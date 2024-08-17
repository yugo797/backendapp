from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.location import Location, LocationCreate
from crud.location import get_location, create_location
from database import get_db

router = APIRouter()


@router.post("/", response_model=Location)
def create_new_location(location: LocationCreate, db: Session = Depends(get_db)):
    return create_location(db=db, location=location)


@router.get("/{location_id}", response_model=Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = get_location(db, location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location
