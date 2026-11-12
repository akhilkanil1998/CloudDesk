from app.core.aws import s3_client
from app.core.config import settings
from fastapi import UploadFile
import uuid
import os

def upload_file_to_s3(file:UploadFile) ->str:
    
    
    # generate random id for the file
    file_id = uuid.uuid4()
    
    #extracts the extension of the file
    file_extension = os.path.splitext(file.filename)[1]
    
     # Construct S3 object key
    object_key = f"attachments/{file_id}{file_extension}"
    
    # Upload file to S3
    s3_client.upload_fileobj(
        file.file,
        settings.AWS_S3_BUCKET,
        object_key
    )
    
    return object_key
    