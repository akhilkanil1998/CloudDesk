#this represents the database tables.
from sqlalchemy import String,Integer,DateTime,ForeignKey

from sqlalchemy.orm import Mapped,mapped_column, relationship
# imports the Base class from the database file
from app.core.database import Base
# imports date from the datetime
from datetime import datetime



# User details
class User(Base):
    __tablename__="users"
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    employee_id:Mapped[str] = mapped_column(String(20), unique=True)    
    employee_name:Mapped[str] = mapped_column(String(50))
    email:Mapped[str] = mapped_column(String(100))
    password_hash:Mapped[str] = mapped_column(String(100))
    role_id:Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))
    created_date:Mapped[datetime] = mapped_column(DateTime)

    # relationship with roles table. 
    role = relationship(
        "Role",
        back_populates="users"
    )