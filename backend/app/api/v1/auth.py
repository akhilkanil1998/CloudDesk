# this is like the controller. It accepts the client request and returns the response
from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import LoginRequest,TokenResponse
from app.services.auth_service import AuthenticationService
from app.core.security import create_access_token
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.auth import get_auth_service

#create an endpoint
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# endpoint to login.
@auth_router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    authentication_service: AuthenticationService= Depends(get_auth_service)
    ):

    # Checks if the user email and password are present.
    user = authentication_service.authenticate_user(
        form_data.username,   # This will contain the email
        form_data.password
         )

    #if  User not there, send 401 Unauthorized error
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    
    access_token = create_access_token(subject=str(user.id))
    
    # if user found, return the token values to the client.
    return TokenResponse(
    access_token=access_token,
    token_type="bearer")

