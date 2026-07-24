from fastapi import Depends,HTTPException, status
from app.models.user import User
from app.dependencies.auth import get_current_user 

# Checks if the role of the current user is in the allowed list.
def require_roles(allowed_roles: list[str]):

    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role.role_name not  in  allowed_roles:
            raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
            )
        
        return current_user        
        
    return role_checker
