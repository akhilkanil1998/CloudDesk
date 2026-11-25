from sqlalchemy.orm import Session

from app.models.attachment import Attachment


class AttachmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_attachment(self, attachment: Attachment):
        try:
            self.db.add(attachment)
            self.db.flush()
            return attachment
        except Exception:
            self.db.rollback()
            raise

    def delete_all_attachments_by_ticket_id(self, ticket_id: int):

        attachments = (
            self.db.query(Attachment).filter(Attachment.ticket_id == ticket_id).all()
        )

        for attachment in attachments:
            self.db.delete(attachment)

        return attachments

    def delete_attachment_by_attachment_id(self, attachment_id: int, ticket_id: int):
        attachment = (
            self.db.query(Attachment)
            .filter(Attachment.ticket_id == ticket_id, Attachment.id == attachment_id)
            .first()
        )

        self.db.delete(attachment)
        
        return attachment
