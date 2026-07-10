# this is like the controller. It accepts the client request and returns the response
from fastapi import APIRouter, Depends,HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import LoginRequest,TokenResponse
from app.services.auth_service import AuthenticationService
from app.core.security import create_access_token

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