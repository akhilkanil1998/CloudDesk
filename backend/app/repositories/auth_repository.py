from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password, hash_password

class AuthRepository:
    def __init__(self, db:Session):
          self.db = db

    def authenticate_user(self, email:str, password:str) -> User|None:
        # Fetches the Users from db and filter with email.
                user = self.db.query(User).filter(User.email == email).first()
                if not user:  
                    return None          
                if not verify_password(password, user.password_hash):
                    return None
                
                return user


    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()