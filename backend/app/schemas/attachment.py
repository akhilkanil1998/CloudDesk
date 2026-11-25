from pydantic import BaseModel, ConfigDict


class AttachmentResponse(BaseModel):
    id: int
    file_name: str

    model_config = ConfigDict(from_attributes=True)
