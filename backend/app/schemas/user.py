from pydantic import BaseModel,ConfigDict, EmailStr

# Response to the client when user has been validated using token
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    # Tells pydatnic not to expect dictionary. 
    #  Read the values from the object's attributes.
    #  Usually pdantic expect dictionary.
    model_config = ConfigDict(from_attributes=True)

class CreateUserRequest(BaseModel):        
    full_name: str
    email: EmailStr
    password: str

class UpdateUserRequest(BaseModel):
    full_name: str
    email: EmailStr