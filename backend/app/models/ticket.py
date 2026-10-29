from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy import String,Text,ForeignKey,func,Enum as SQLEnum
from datetime import datetime
from app.enum.priority import Priority
from app.enum.status import Status
from app.models.user import User


class Ticket(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100)) 
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[Status] = mapped_column(SQLEnum(Status,
                                                   name="status",
                                                   values_callable=lambda enum_cls: [
                                                    member.value for member in enum_cls
                                                ],), default="Open")
    priority: Mapped[Priority] = mapped_column(SQLEnum(Priority),default="Low")
    created_on: Mapped[datetime] = mapped_column(server_default=func.now())
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    modified_on: Mapped[datetime] = mapped_column(server_default=func.now(),onupdate=func.now())
    modified_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    assigned_to: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    assigned_user: Mapped["User | None"] = relationship("User", foreign_keys=[assigned_to])
    created_user: Mapped["User|None"] = relationship("User", foreign_keys=[created_by])
    modified_user: Mapped["User|None"] = relationship("User", foreign_keys=[modified_by])