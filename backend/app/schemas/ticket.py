from pydantic import BaseModel, ConfigDict, AliasPath, Field
from app.enum.priority import Priority
from app.enum.status import Status

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    assigned_to: int | None
    assigned_to_name: str | None = Field(
        default=None,
        validation_alias=AliasPath("assigned_user", "employee_name"),
    )
    created_by: int | None=None
    created_by_name: str | None=Field(
        default=None,
        validation_alias=AliasPath("created_user", "employee_name"),
    )
    modified_by: int | None=None
    modified_by_name: str | None=Field(
        default=None,
        validation_alias=AliasPath("modified_user", "employee_name"),
    )
    model_config = ConfigDict(from_attributes=True)



class CreateTicketRequest(BaseModel):
    title: str
    description: str
    priority: Priority = Priority.Low #default to Low priority


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