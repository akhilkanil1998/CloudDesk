from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password, hash_password

class AuthenticationService:

    @staticmethod
    def authenticate_user( email:str, password:str, db:Session):
        # Fetches the Users from db and filter with email.
        user = db.query(User).filter(User.email == email).first()
        if not user:  
            return None          
        if not verify_password(password, user.password_hash):
            return None
        
        return user

    @staticmethod
    def get_user_by_id(user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()

        
       



