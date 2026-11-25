import os
import uuid

from botocore.exceptions import ClientError
from fastapi import UploadFile,File

from app.core.aws import s3_client
from app.core.config import settings
from app.core.logging_config import logger


def upload_file_to_s3(folder_name: str, files: list[UploadFile] = File(default=[])) -> list[str]:
    uploaded_keys = []
    for file in files:
        # generate random id for the file
        file_id = uuid.uuid4()

        # extracts the extension of the file
        file_extension = os.path.splitext(file.filename)[1]

        # Construct S3 object key
        object_key = f"attachments/{folder_name}/{file_id}{file_extension}"
        try:
            # Upload file to S3
            s3_client.upload_fileobj(file.file, settings.AWS_S3_BUCKET, object_key)
            uploaded_keys.append(object_key)

        except ClientError:
            logger.exception("Error uploading file to AWS S3 bucket.")
            raise
    return uploaded_keys


# deletes file from s3
def delete_file_from_s3(s3_object_key: str, folder_name: str):

    try:
        s3_client.delete_object(
            Bucket=settings.AWS_S3_BUCKET, Key=f"{folder_name}/{s3_object_key}"
        )
    except ClientError:  # noqa: TRY203
        raise
