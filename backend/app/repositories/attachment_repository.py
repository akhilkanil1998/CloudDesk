from app.models.attachment import Attachment
from sqlalchemy.orm import Session


class AttachmentRepository():
    def __init__(self, db:Session):
         self.db = db
        
    
    def create_attachment(self,attachment: Attachment):
        self.db.add(attachment)
        self.db.flush()
        return attachment
        