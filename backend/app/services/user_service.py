from sqlalchemy.orm import Session 
from app.models.user import User
from app.schemas.user import CreateUserRequest
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException,status
from app.core.security import hash_password
from datetime import datetime

class UserService:
    @staticmethod
    def get_all_users(db:Session) -> list[User]:
        return UserRepository.get_all_users(db)
    
    
    @staticmethod
    def create_user(db:Session, request:CreateUserRequest) -> User:
        existing_user = UserRepository.get_user_by_email(db, request.email)

        if existing_user is not None:
            raise HTTPException (
                status_code = status.HTTP_409_CONFLICT,
                detail = "A user with this email already exists."
            )
        
        existing_role = RoleRepository.get_role_by_id(request.role_id)

        if role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found."
            )
        
        
        hashed_password = hash_password(request.password)
        new_user = User(
            employee_name = request.full_name,
            email = request.email,
            password_hash = hashed_password,
            role_id = existing_role.id         
        )
        created_user = UserRepository.create_user(db, new_user)
        # generates the emp id
        created_user.employee_id = f"CD-{created_user.id:04d}"

        # save the user with the generated emp id.
        created_user = UserRepository.save_user_changes(db,created_user)
        return created_user
           

            


