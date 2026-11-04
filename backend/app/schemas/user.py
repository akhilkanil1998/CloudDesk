from pydantic import BaseModel,ConfigDict, EmailStr, field_validator
from typing import Optional

# Response to the client when user has been validated using token
class UserResponse(BaseModel):
    employee_id: str
    email: EmailStr
    first_name: str
    last_name: str
    role: str
    
    @field_validator("role", mode="before")
    @classmethod
    def get_role_name(cls, value):
        return value.name if hasattr(value, "name") else value


    # Tells pydatnic not to expect dictionary. 
    #  Read the values from the object's attributes.
    #  Usually pdantic expect dictionary.
    model_config = ConfigDict(from_attributes=True)

class CreateUserRequest(BaseModel):        
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role_id: int

    # Request to partially update a user
class UpdateUserRequest(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    role_id: int | None = None