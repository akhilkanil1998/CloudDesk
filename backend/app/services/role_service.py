from app.repositories.role_repository import RoleRepository
from app.models.roles import Role
class RoleService:
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository
    
    def get_role_by_id(self, role_id: int) -> Role|None:
        return self.role_repository.get_role_by_id(role_id)