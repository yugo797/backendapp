from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from auth import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        raise ValueError("Email already registered")

    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_obj: User, obj_in: UserUpdate) -> User:
    if obj_in.password:
        db_obj.hashed_password = get_password_hash(obj_in.password)
    if obj_in.name:
        db_obj.name = obj_in.name
    if obj_in.email:
        db_obj.email = obj_in.email
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
