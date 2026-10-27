from app.repositories.auth_repository import AuthRepository
from app.models.user import User
from app.core.logging_config import logger

class AuthenticationService:
    def __init__(self, auth_repository:AuthRepository):
        self.auth_repository = auth_repository
    
    def authenticate_user( self, email:str, password:str) -> User|None:
        user = self.auth_repository.authenticate_user(email,password)
        if user:
            logger.info(f"User {user.employee_name}, {user.employee_id} has logged in successfully.")
        return user
        

    
    # def get_user_by_id(self, user_id: int):
    #     return self.auth_repository.get_user_by_id(user_id)

        
       



