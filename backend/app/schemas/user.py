from pydantic import BaseModel,ConfigDict

# Response to the client when user has been validated using token
class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str

    # Tells pydatnic not to expect dictionary. 
    #  Read the values from the object's attributes.
    #  Usually pdantic expect dictionary.
    model_config = ConfigDict(from_attributes=True)