from sqlalchemy.orm import Session
from app.models.roles import Role

class RoleRepository:
    def __init__(self,db:Session):
            self.db = db

    def get_role_by_id(self, role_id: int) -> Role|None:
          return{
                self.db.query(Role)
                .filter(Role.id == role_id)
                .first()
          }
          
    