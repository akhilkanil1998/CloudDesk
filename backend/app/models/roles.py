
from app.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,String

# Roles for the users.
class Role(Base):
    __tablename__="roles"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name:Mapped[str] = mapped_column(String(20), unique=True)

    # relationship with user table. 
    users = relationship(
        "User",
        back_populates="role"
    )