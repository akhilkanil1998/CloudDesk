from app.services.ticket_service import TicketService
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.repositories.ticket_repository import TicketRepository

def get_ticket_repository(db:Session = Depends(get_db)) -> TicketRepository:
    return TicketRepository(db=db)


def get_ticket_service(ticket_repository: TicketRepository = Depends(get_ticket_repository)) -> TicketService:
    return TicketService(ticket_repository=ticket_repository)
