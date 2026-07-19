from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.db.database import get_db
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from app.core.config import settings
from app.models.user import User

#This extracts the Bearer token from the request header.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

#  Gets the current user verifying the jwt token and checking the user in db.
def get_current_user(token: str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
    # initializing the exception here to use in multiple places.
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        # When FastAPI returns 401 Unauthorized, this header tells clients that
        # This endpoint expects Bearer Token authentication.
        # Swagger uses this header to understand the authentication scheme.
        # Without it, some clients won't know they should send a Bearer token.          
        headers={"WWW-Authenticate":"Bearer"},
    )

    try:
        # Verifies the token signature using the secret key. 
        # Checks whether the token has expired (exp claim).
        # Validates that the token structure is correct.
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
    
        
        try:
            # gets the sub value from payload and store it as user_id. 
            # Converting to int as the payload returns as json string.
            user_id = int(payload.get("sub"))

        except(TypeError, ValueError):
            raise credentials_exception
        
        # if sub is not available in the payload also it will decode. 
        # So rejecting if user id is none.
        if user_id is None:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
        
    # fetching the user from the database.
    user = db.query(User).filter(User.id == user_id).first()

        # Raie error if user is none.
    if user is None:
        raise credentials_exception

    return user
        
    
    
   

    