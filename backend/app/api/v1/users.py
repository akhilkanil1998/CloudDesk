# this is like the controller. It accepts the client request and returns the response
from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.dependencies.permissions import require_roles
from app.models.user import User
from app.schemas.user import UserResponse
from app.services.user_service import UserService
from app.dependencies.user import get_user_service
from app.schemas.user import CreateUserRequest

#create an endpoint
user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

# Who am I based on the access token I provided?
# First the Depends method will run and then the value will be stored to current_user
@user_router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return UserResponse(
        employee_id=current_user.employee_id,
        email=current_user.email,
        employee_name=current_user.employee_name,
        role=current_user.role.role_name
    )

# current_user is injected by FastAPI.
# The dependency authenticates the user and authorizes
# that they have the required role before this endpoint executes.
@user_router.get("/users", response_model= list[UserResponse])
def get_all_users(user_service: UserService = Depends(get_user_service), 
                  admin_user: User = Depends(require_roles(["Admin"]))):
    return user_service.get_all_users()

@user_router.post("/create_user")
def create_user( create_user_request: CreateUserRequest, user_service: UserService = Depends(get_user_service)):
        return user_service.create_user(create_user_request)


@user_router.get("/get_user_by_id", response_model=UserResponse)
def get_user_by_id(userid: int,user_service: UserService = Depends(get_user_service),
                   admin_user: User = Depends(require_roles(["Admin"]))):
     user = user_service.get_user_by_id(userid=userid)
     return UserResponse(
            employee_id=user.employee_id,
            email=user.email,
            employee_name=user.employee_name,
            role=user.role.role_name)