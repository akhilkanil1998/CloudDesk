#Create and manage the database connection and provide database 
# sessions to the rest of the application.
from sqlalchemy import create_engine

# sessionmaker - Creates database sessions.
# DeclarativeBase - Base class for all models.Helps to create orm for the class properties
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings

# Engine is the bridge between the app and the db, like a connection manager. 
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG
)
# Session Factory
# A session represents one conversation with the database.
SessionLocal = sessionmaker(
    bind= engine,
    autoflush= False,
    autocommit = False
)

# Base class for all models
class Base(DeclarativeBase):
    pass

# Dependency to create a database session
def get_db():
    # creating a session
    db = SessionLocal()
    try:
        #Pauses execution and saves state to resume later.
        yield db
    # closes the connection even if there is error.
    finally:
        db.close()
