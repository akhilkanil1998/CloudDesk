# this is like the controller. It accepts the client request and returns the response
from fastapi import APIRouter, Depends
from app.dependency.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse

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