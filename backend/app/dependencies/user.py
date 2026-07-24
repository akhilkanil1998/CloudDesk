from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.repositories.role_repository import RoleRepository
from app.services.user_service import UserService
from fastapi import Depends
from app.db.database import get_db
from app.dependencies.role import get_role_repository

# this will tell fastapi to create User Repository. This is a factory function.
def get_user_repository(db: Session= Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_service(user_repository: UserRepository = Depends(get_user_repository),
                     role_repository:RoleRepository = Depends(get_role_repository)
                     ) -> UserService:
    return UserService(user_repository,role_repository)

