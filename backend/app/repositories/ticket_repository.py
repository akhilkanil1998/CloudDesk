from app.models.ticket import Ticket
from sqlalchemy.orm import Session
from sqlalchemy import and_
class TicketRepository():
    def __init__(self, db:Session):
        self.db = db


    def create_ticket(self, ticket:Ticket):
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def get_all_tickets(self) -> list[Ticket]|None:
       return self.db.query(Ticket).all()

    def get_all_tickets_by_assignee(self, user_id: int) -> list[Ticket]|None:
        return self.db.query(Ticket).filter(Ticket.assigned_to == user_id)

    def get_all_tickets_by_created_user(self,user_id: int) -> list[Ticket]|None:
        return self.db.query(Ticket).filter(Ticket.created_by==user_id)

    def get_ticket_by_id(self,id: int) -> Ticket|None:
        return self.db.get(Ticket,id)


    def get_ticket_by_id_and_assignee(self, id, user_id: int) -> Ticket|None:
        return self.db.query(Ticket).filter(and_(Ticket.id == id, 
                                                 Ticket.assigned_to == user_id)).one_or_none()

    
    def get_ticket_by_id_and_created(self, id, user_id: int) -> Ticket|None:
            return self.db.query(Ticket).filter(and_(Ticket.id == id, 
                                                     Ticket.created_by == user_id)).one_or_none()


