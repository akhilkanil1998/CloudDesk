from enum import Enum

class TicketQueryScope(Enum):
    ALL = "ALL"
    ASSIGNED = "ASSIGNED"
    CREATED = "CREATED"
    