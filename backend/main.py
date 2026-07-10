# imports the Fast Api package
from fastapi import FastAPI
from app.api.v1.auth import auth_router
# Import all models so SQLAlchemy registers them
import app.models

# Instance of FastAPI
app = FastAPI()

app.include_router(auth_router)