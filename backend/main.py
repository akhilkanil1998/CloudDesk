# imports the Fast Api package
from fastapi import FastAPI
from app.api.v1.auth import auth_router
from app.api.v1.users import user_router
# Import all models so SQLAlchemy registers them
import app.models

# Instance of FastAPI
app = FastAPI()
# this will include the router in the auth file.
app.include_router(auth_router)
app.include_router(user_router)
