from botocore.exceptions import BotoCoreError, ClientError
from fastapi import File, HTTPException, UploadFile
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.logging_config import logger
from app.models.user import User
from app.repositories.attachment_repository import AttachmentRepository
from app.utils.aws_s3_utils import delete_file_from_s3, upload_file_to_s3
from app.models.attachment import Attachment


class AttachmentService:
    def __init__(self, db: Session, attachment_repository: AttachmentRepository):
        self.db = db
        self.attachment_repository = attachment_repository

    def create_attachment(
        self,
        ticket_id: int,
        current_user: User,
        files: list[UploadFile] = File(default=[]),
    ) -> str:

        for file in files:
            try:
                file_object_key = upload_file_to_s3(files=files, folder_name=ticket_id)

                self.attachment_repository.create_attachment(
                    Attachment(
                        ticket_id=ticket_id,
                        file_name=file.filename,
                        s3_object_key=file_object_key,
                        uploaded_by=current_user.id,
                    )
                )

            except (
                SQLAlchemyError,
                BotoCoreError,
                ClientError,
                HTTPException,
                OSError,
                RuntimeError,
                ValueError,
            ):
                self.db.rollback()

                if file_object_key:
                    try:
                        delete_file_from_s3(file_object_key, folder_name=ticket_id)
                    except (BotoCoreError, ClientError, OSError, RuntimeError):
                        logger.exception("Failed to clean up uploaded S3 object")

                raise

    # Deletes the attachments in the ticket
    def delete_all_attachments_by_ticket_id(self, ticket_id: int):

        try:
            attachments = (
                self.attachment_repository.delete_all_attachments_by_ticket_id(
                    ticket_id=ticket_id
                )
            )

            if attachments:
                for attachment in attachments:
                    delete_file_from_s3(
                        folder_name=attachment.ticket_id,
                        s3_object_key=attachment.s3_object_key,
                    )
                    logger.info(f"Attachment {attachment.id} deleted successfully.")

            if not attachment:
                raise HTTPException(status_code=404, detail="Attachment not found")
        except (
            SQLAlchemyError,
            BotoCoreError,
            ClientError,
            HTTPException,
            OSError,
            RuntimeError,
            ValueError,
        ):
            self.db.rollback()
            logger.exception("Unable to delete attachment")
            raise

    def delete_attachment_by_attachment_id(self, attachment_id: int, ticket_id: int):

        try:
            attachment = self.attachment_repository.delete_attachment_by_attachment_id(
                attachment_id=attachment_id, ticket_id=ticket_id
            )

            if attachment:
                delete_file_from_s3(
                    folder_name=attachment.ticket_id,
                    s3_object_key=attachment.s3_object_key,
                )
                self.db.commit()
                logger.info(f"Attachment {attachment.id} deleted successfully.")

            if not attachment:
                raise HTTPException(status_code=404, detail="Attachment not found")

        except (
            SQLAlchemyError,
            BotoCoreError,
            ClientError,
            HTTPException,
            OSError,
            RuntimeError,
            ValueError,
        ):
            self.db.rollback()
            logger.exception("Unable to delete attachment")
            raise
