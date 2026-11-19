from app.core.aws import s3_client
from app.core.config import settings
from fastapi import UploadFile
import uuid
import os
from app.core.logging_config import logger
from botocore.exceptions import ClientError

def upload_file_to_s3(file:UploadFile) ->str:
        
    # generate random id for the file
    file_id = uuid.uuid4()
    
    #extracts the extension of the file
    file_extension = os.path.splitext(file.filename)[1]
    
     # Construct S3 object key
    object_key = f"attachments/{file_id}{file_extension}"
    try:
        # Upload file to S3
        s3_client.upload_fileobj(
            file.file,
            settings.AWS_S3_BUCKET,
            object_key
        )
        return object_key  
        
    
    except ClientError:
        logger.exception("Error uploading file to AWS S3 bucket.")
        raise 
    
# delete the file from s3
def delete_file_from_s3(s3_object_key):
    
    try:
        s3_client.delete_object(
            Bucket=settings.AWS_S3_BUCKET,
            Key= s3_object_key
        )
    except ClientError:
        raise