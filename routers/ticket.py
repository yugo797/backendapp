from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.ticket import Ticket, TicketCreate, TicketUpdate
from crud.ticket import get_ticket, create_ticket, get_tickets_by_user, get_all_tickets, update_ticket, delete_ticket
from database import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=Ticket)
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db=db, ticket=ticket)


@router.get("/{ticket_id}", response_model=Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = get_ticket(db, ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket


@router.get("/{user_id}", response_model=Ticket)
def read_ticket_by_ticket(user_id: int, db: Session = Depends(get_db)):
    db_ticket = get_tickets_by_user(db, user_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket


@router.get("/", response_model=List[Ticket])
def read_all_tickets(db: Session = Depends(get_db)):
    return get_all_tickets(db)


@router.put("/{ticket_id}", response_model=Ticket)
def update_existing_ticket(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    db_ticket = update_ticket(
        db=db, ticket_id=ticket_id, ticket=ticket)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket


@router.delete("/{ticket_id}", response_model=Ticket)
def delete_existing_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = delete_ticket(db, ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket
