from fastapi import APIRouter,Depends
from app.schemas.ticket import CreateTicketRequest, TicketResponse
from app.services.ticket_service import TicketService
from app.dependencies.tickets import get_ticket_service
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.ticket import UpdateTicketRequest


ticket_router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@ticket_router.post("/tickets")
def create_ticket(ticket: CreateTicketRequest, 
                  ticket_service: TicketService = Depends(get_ticket_service),
                  current_user: User= Depends(get_current_user)):
    ticket_service.create_ticket(ticket=ticket, current_user=current_user)


@ticket_router.get("/tickets", response_model= list[TicketResponse])
def get_all_tickets(ticket_service: TicketService = Depends(get_ticket_service),
                  current_user: User= Depends(get_current_user)):
    return ticket_service.get_all_tickets(current_user)

@ticket_router.get("tickets", response_model= TicketResponse)
def get_ticket_by_id(id: int, ticket_service: TicketService = Depends(get_ticket_service),
                     current_user: User=Depends(get_current_user)):
    return ticket_service.get_ticket_by_id(id,current_user=current_user)

@ticket_router.patch("ticket", response_model=TicketResponse)
def update_ticket_by_id(id: int, update_request: UpdateTicketRequest, ticket_service: TicketService = Depends(get_ticket_service),
                     current_user: User=Depends(get_current_user)):
    return ticket_service.update_ticket_by_id(id, update_request=update_request, current_user=current_user)

