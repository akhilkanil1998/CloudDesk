from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.role_repository import RoleRepository

def get_role_repository(db: Session= Depends(get_db)) -> RoleRepository:
    return RoleRepository(db)