from app.services.ticket_service import TicketService
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.repositories.ticket_repository import TicketRepository
from app.repositories.attachment_repository import AttachmentRepository

def get_ticket_repository(db:Session = Depends(get_db)) -> TicketRepository:
    return TicketRepository(db=db)

def get_attachment_repository(
    db: Session = Depends(get_db)
) -> AttachmentRepository:
    return AttachmentRepository(db=db)

def get_ticket_service(db: Session = Depends(get_db),ticket_repository: TicketRepository = Depends(get_ticket_repository),
                        attachment_repository: AttachmentRepository = Depends(get_attachment_repository)) -> TicketService:
    return TicketService(db=db,ticket_repository=ticket_repository,
                         attachment_repository=attachment_repository)
