from sqlalchemy.orm import Session 
from app.models.user import User
from app.schemas.user import CreateUserRequest
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException,status
from app.core.security import hash_password
from datetime import datetime
from app.repositories.role_repository import RoleRepository

class UserService:
    def __init__(self, user_repository: UserRepository,role_repository: RoleRepository):
        self.user_repository = user_repository
        self.role_repository = role_repository
    
    def get_all_users(self) -> list[User]:
        return self.user_repository.get_all_users()
    
    
   
    def create_user(self, request:CreateUserRequest) -> User:
        existing_user = self.user_repository.get_user_by_email(request.email)

        if existing_user is not None:
            raise HTTPException (
                status_code = status.HTTP_409_CONFLICT,
                detail = "A user with this email already exists."
            )
        
        existing_role = self.role_repository.get_role_by_id(request.role_id)

        if existing_role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found."
            )
        
        
        hashed_password = hash_password(request.password)
        # get the next emp id sequence 
        sequence = self.user_repository.get_next_emp_sequence()

        generated_employee_id = f"CD-{sequence:04d}"
        new_user = User(
            employee_id = generated_employee_id,
            employee_name = request.full_name,
            email = request.email,
            password_hash = hashed_password,
            role_id = request.role_id       
        )
        created_user = self.user_repository.create_user(new_user)   

        # # save the user with the generated emp id.
        # created_user = self.user_repository.save_user_changes(created_user)
        return created_user
           

            


