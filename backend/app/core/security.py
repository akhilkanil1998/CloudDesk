from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashes the given password.
def hash_password(password: str) -> str: # Create a new string object from the given object.
    return pwd_context.hash(password)

# checks the password provided with the hashed password in the db. Returns true if it is same.
def verify_password(password:str, hashed_password:str):
    return pwd_context.verify(password,hashed_password)

# create jwt token, subject is the parameter which the token should be created like userid.
def create_access_token(subject: str):
    current_time = datetime.now(timezone.utc)
    # fetches value from the env file
    expiry_time = current_time + timedelta(minutes=settings.access_token_expire_minutes)

    payload = {
        "sub": subject,
        "exp": expiry_time
    }

    encoded_jwt = jwt.encode(claims= payload, key= settings.jwt_secret_key , algorithm= settings.jwt_algorithm)
    return encoded_jwt
