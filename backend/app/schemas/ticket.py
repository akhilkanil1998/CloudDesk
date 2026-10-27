from pydantic import BaseModel, ConfigDict
from app.enum.priority import Priority
from app.enum.status import Status

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    model_config = ConfigDict(from_attributes=True)



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

class PaginatedTicketResponse(BaseModel):
    items: list[TicketResponse]
    page: int
    page_size: int
    total: int
    total_pages: int