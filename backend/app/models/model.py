#this represents the database tables.

from sqlalchemy import String

from sqlalchemy.orm import Mapped,mapped_column
# imports the Base class from the database file
from app.core.database import Base

class User(Base):
    __tablename__="user"
    id:Mapped[int] = mapped_column(primary_key=True)
    employee_id:Mapped[String] = mapped_column(unique=True)    
    employee_name:Mapped[String] = mapped_column()