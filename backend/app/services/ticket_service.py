from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import CreateTicketRequest, TicketResponse,PaginatedTicketResponse
from app.models.ticket import Ticket
from app.models.user import User
from app.schemas.ticket import UpdateTicketRequest
from fastapi import HTTPException,status
from app.enum.ticketQueryScope import TicketQueryScope
from app.enum.status import Status
from app.enum.priority import Priority
from app.core.logging_config import logger

class TicketService:
    def __init__(self, ticket_repository:TicketRepository):
        self.ticket_repository = ticket_repository

    def create_ticket(self,ticket:CreateTicketRequest, current_user:User) -> TicketResponse:
        ticket = Ticket(title = ticket.title, 
                        description= ticket.description,
                        priority = ticket.priority,
                        created_by = current_user.id)
        
        response_ticket = self.ticket_repository.create_ticket(ticket=ticket)
        logger.info(f"Ticket {response_ticket.id} created successfully. User id {current_user.employee_id}")
        return response_ticket


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

        elif(current_user.role.role_name == "Agent"):
            return self.ticket_repository.get_ticket_by_id_and_assignee(id=id, user_id=current_user.id)

        elif(current_user.role.role_name == "User"):
                    return self.ticket_repository.get_ticket_by_id_and_created(id=id, user_id=current_user.id)


    def update_ticket_by_id(self, id: int, current_user: User, 
                            update_request: UpdateTicketRequest) -> Ticket|None:

        user_role = current_user.role.role_name
        # only the user provided values. Other fields are none
        update_data = update_request.model_dump(exclude_unset=True)

        # No validation for Admin
        if user_role == "Admin":
            return self.ticket_repository.update_ticket_by_id(id, update_request=update_request)

        # Fetches the ticket by id and checks the user is authorized to perform changes
        ticket = self.get_ticket_by_id(id, current_user=current_user)

        if user_role == "Agent":

            if not ticket:
                return None
            # forbidden_fields set to tell that it will be rejected.
            forbidden_fields = {"assigned_to"}

            

        elif user_role == "User":    
            
            forbidden_fields = {
                "priority", "status", "assigned_to"
                }          

            
        else:             
            raise HTTPException(
            status_code=403,
            detail="You are not authorized to update tickets."
            )

        requested_forbidden_fields = (
            forbidden_fields & update_data.keys()
            )

        if requested_forbidden_fields:
            raise HTTPException(
                status_code=403,
                detail=(
                    "You cannot update these fields: "
                    + ", ".join(sorted(requested_forbidden_fields))
                )
            )

        return self.ticket_repository.update_ticket_by_id(id, update_request = update_request)
         
    def delete_ticket_by_id(self, ticket_id: int, current_user:User):
        ticket = self.get_ticket_by_id(ticket_id, current_user=current_user)

        if not ticket:
            raise  HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Ticket {ticket_id} not found."
                )

        # agents cant delete
        if current_user.role.role_name not in ["Admin", "User"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to delete this ticket."
            )
                                
        is_deleted = self.ticket_repository.delete_ticket_by_id(
                    ticket_id=ticket_id)

    
        if not is_deleted:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket {ticket_id} could not be deleted because it no longer exists."
            )

       
        return f"Ticket {ticket_id} deleted successfully."



    def get_tickets_query(self,page: int, page_size: int,
                          current_user: User,
                          status: Status | None, 
                          priority:Priority|None) -> PaginatedTicketResponse:

        user_id = current_user.id

        if current_user.role.role_name == "Agent":
            scope = TicketQueryScope.ASSIGNED

        elif current_user.role.role_name == "User":
            scope = TicketQueryScope.CREATED

        elif current_user.role.role_name == "Admin":
            scope = TicketQueryScope.ALL

        else:
            raise HTTPException(status_code=403, detail="Invalid user role")

        total, tickets = self.ticket_repository.get_tickets_query(scope=scope,page=page,page_size=page_size,
                                                            user_id=user_id,
                                                           status=status,priority=priority)
        total_pages = (total + page_size - 1) // page_size

        ticket_items = [
        TicketResponse.model_validate(ticket)
        for ticket in tickets
    ]

        return PaginatedTicketResponse(
        items=ticket_items,
        page=page,
        page_size=page_size,
        total=total,
        total_pages=total_pages
    )

        


        

       
        
