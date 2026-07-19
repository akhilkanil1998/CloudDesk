from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from fastapi import Depends
from app.db.database import get_db

# this will tell fastapi to create User Repository
def get_user_repository(db: Session= Depends(get_db)) -> UserRepository:
    return UserRepository(db)

