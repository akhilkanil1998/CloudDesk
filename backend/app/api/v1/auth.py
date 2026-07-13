# this is like the controller. It accepts the client request and returns the response
from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import LoginRequest,TokenResponse
from app.services.auth_service import AuthenticationService
from app.core.security import create_access_token
from app.dependency.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse

#create an endpoint
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# endpoint to login.
@auth_router.post("/login", response_model=TokenResponse)
def login(request:LoginRequest, db:Session=Depends(get_db)):
    # Checks if the user email and password are present.
    user = AuthenticationService.authenticate_user(request.email, request.password, db)

    #if  User not there, send 401 Unauthorized error
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid email or password.")
    
    access_token = create_access_token(subject=str(user.id))
    
    # if user found, return the token values to the client.
    return TokenResponse(
    access_token=access_token,
    token_type="bearer")

# Who am I based on the access token I provided?
# First the Depends method will run and then the value will be stored to current_user
@auth_router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user