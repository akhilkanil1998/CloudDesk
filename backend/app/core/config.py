# Reads configuration
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    #project details
    PROJECT_NAME:str
    VERSION:str
    DEBUG:bool
    
    # API
    API_V1_PREFIX: str

     # Database
    DATABASE_URL: str  

    jwt_secret_key: str
    jwt_algorithm:str
    access_token_expiry_minutes:int   

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore" # ignores any other values from .env file comparing with the Settings class.

    )

# creating object of Settings to get the values from the .env file.
# This object is used in other classes so that no new object is created for the same in other classes.     
settings = Settings()
