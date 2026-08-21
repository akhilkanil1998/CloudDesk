from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Text,ForeignKey,func
from datetime import datetime

class Ticket(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100)) 
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="OPEN")
    priority: Mapped[str] = mapped_column(String(50),default="LOW")
    created_on: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    modified_on: Mapped[datetime] = mapped_column(server_default=func.now(),onupdate=func.now())
    modified_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)