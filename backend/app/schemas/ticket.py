from pydantic import BaseModel
from app.enum.priority import Priority
from app.enum.status import Status

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str



class CreateTicketRequest(BaseModel):
    title: str
    description: str
    priority: Priority = Priority.LOW #default to Low priority


class UpdateTicketRequest(BaseModel): 
    title: str | None=None
    description: str | None=None
    priority: Priority | None=None
    status: Status | None=None
    assigned_to: int | None=None