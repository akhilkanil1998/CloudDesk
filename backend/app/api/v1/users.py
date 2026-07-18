# this is like the controller. It accepts the client request and returns the response
from fastapi import APIRouter, Depends
from app.dependency.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import UserService

#create an endpoint
user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

# Who am I based on the access token I provided?
# First the Depends method will run and then the value will be stored to current_user
@user_router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# current_user is for the authentication. Even though we don't 
# reference current_user inside the function, the dependency itself enforces authentication.
@user_router.get("/users", response_model= list[UserResponse])
def get_all_users(db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return UserService.get_all_users(db)