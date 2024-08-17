from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.category import Category, CategoryCreate
from crud.category import get_category, create_category
from database import get_db

router = APIRouter()


@router.post("/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)


@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
