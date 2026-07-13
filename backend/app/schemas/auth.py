# pydantic will create these 
from pydantic import BaseModel,EmailStr

# Same like DTO, for the login
class LoginRequest(BaseModel):
    email:EmailStr
    password:str

# Response sent to the client
class TokenResponse(BaseModel):
    access_token:str
    token_type:str

