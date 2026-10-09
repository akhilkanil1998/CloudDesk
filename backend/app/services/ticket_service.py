from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import CreateTicketRequest, TicketResponse
from app.models.ticket import Ticket
from app.models.user import User

class TicketService:
    def __init__(self, ticket_repository:TicketRepository):
        self.ticket_repository = ticket_repository

    def create_ticket(self,ticket:CreateTicketRequest, current_user:User) -> TicketResponse:
        ticket = Ticket(title = ticket.title, 
                        description= ticket.description,
                        priority = ticket.priority,
                        created_by = current_user.id)
        return self.ticket_repository.create_ticket(ticket=ticket)


    def get_all_tickets(self,current_user:User) -> list[Ticket]|None:
        

        if(current_user.role.role_name == "Admin" ):
            return self.ticket_repository.get_all_tickets()
            

        if(current_user.role.role_name == "Agent"):
            return self.ticket_repository.get_all_tickets_by_assignee(current_user.id)

        if(current_user.role.role_name == "User"):
            return self.ticket_repository.get_all_tickets_by_created_user(current_user.id)
        

    def get_ticket_by_id(self,id,current_user: User) -> Ticket|None:
        if(current_user.role.role_name == "Admin" ):
            return self.ticket_repository.get_ticket_by_id(id=id)

        if(current_user.role.role_name == "Agent"):
            return self.ticket_repository.get_ticket_by_id_and_assignee(id=id, user_id=current_user.id)

        if(current_user.role.role_name == "User"):
                    return self.ticket_repository.get_ticket_by_id_and_created(id=id, user_id=current_user.id)