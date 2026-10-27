from app.models.ticket import Ticket
from sqlalchemy.orm import Session,Query
from sqlalchemy import and_
from app.schemas.ticket import UpdateTicketRequest, PaginatedTicketResponse
from app.enum.ticketQueryScope import TicketQueryScope
from app.enum.status import Status
from app.enum.priority import Priority

class TicketRepository():
    def __init__(self, db:Session):
        self.db = db


    def create_ticket(self, ticket:Ticket):
        try:
            self.db.add(ticket)
            self.db.commit()
            self.db.refresh(ticket)

        except Exception:
            self.db.rollback()
            raise 

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


    def update_ticket_by_id(self,id: int, update_request: UpdateTicketRequest) -> Ticket|None:        
        
        ticket = self.get_ticket_by_id(id=id)


        if ticket is None:
            return None

        # fetches only the values sent by the user. If user did not add a value, then it is rejected.
        update_data = update_request.model_dump(exclude_unset=True, exclude_none=True)
        
        for key, value in update_data.items():
            setattr(ticket,key,value)

        self.db.commit()
        self.db.refresh(ticket)

        return ticket


    def delete_ticket_by_id(self, ticket_id: int) -> bool:  

        ticket = self.get_ticket_by_id(ticket_id)

        if ticket is None:
            return False
        try:
            self.db.delete(ticket)
            self.db.commit()
            return True

        except Exception:
            self.db.rollback()
            raise 

       
    def get_tickets_query(self, scope: TicketQueryScope, 
                           page: int, page_size: int,
                            user_id: int | None = None,
                            status: Status | None=None,
                            priority: Priority | None=None) -> tuple[int, list[Ticket]]:
        # Fetches all the tickets
        query = self.db.query(Ticket)

        if scope == TicketQueryScope.ASSIGNED:
            if user_id is None:
                raise ValueError("user_id is required for ASSIGNED scope")
            # modify the filter query with assigned
            query = query.filter(Ticket.assigned_to == user_id)

        elif scope == TicketQueryScope.CREATED:
            if user_id is None:
                raise ValueError("user_id is required for CREATED scope")
             # modify the filter query with created
            query = query.filter(Ticket.created_by == user_id)

        elif scope != TicketQueryScope.ALL:
            raise ValueError(f"Unsupported ticket query scope: {scope}")
        
        if status is not None:
            query = query.filter(Ticket.status == status)

        if priority is not None:
            query = query.filter(Ticket.priority == priority)

        # fetches the count of the records after the filtering
        total = query.count()
        offset = (page - 1) * page_size

        # ordering the tickets based on the page.
        tickets = (
        query
        .order_by(Ticket.created_on.desc(), Ticket.id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
        )

        return total, tickets




        


        



