from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, func
from datetime import datetime


class Attachment(Base):
    __tablename__ = "attachments"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))
    file_name: Mapped[str] = mapped_column(String(200))
    s3_object_key: Mapped[str] = mapped_column(String(500),unique=True, nullable=False)
    uploaded_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    uploaded_on: Mapped[datetime] = mapped_column(server_default=func.now())
    
    ticket = relationship(
        "Ticket",
        back_populates="attachments"
    )