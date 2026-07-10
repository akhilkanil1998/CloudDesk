from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password, hash_password

class Authentication_Service:
    
    @staticmethod
    def authenticate_user( email:str, password:str, db:Session):
        user = db.query(User).filter(User.email == email).first()
        if not user:  
            return None          
        if not verify_password(password, user.password_hash):
            return None
        
        return user


        
       



