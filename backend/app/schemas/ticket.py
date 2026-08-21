from pydantic import BaseModel

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str