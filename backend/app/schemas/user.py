from pydantic import BaseModel,ConfigDict, EmailStr
from typing import Optional

# Response to the client when user has been validated using token
class UserResponse(BaseModel):
    employee_id: str
    email: EmailStr
    employee_name: str

    # Tells pydatnic not to expect dictionary. 
    #  Read the values from the object's attributes.
    #  Usually pdantic expect dictionary.
    model_config = ConfigDict(from_attributes=True)

class CreateUserRequest(BaseModel):        
    full_name: str
    email: EmailStr
    password: str
    role_id: int

class UpdateUserRequest(BaseModel):
    full_name: str
    email: EmailStr

class UpdateUserRequest(BaseModel):        
    full_name: Optional[str] = None
    role_id: Optional[int] = None