from dataclasses import Field
from pydantic import BaseModel

class OAuth2PasswordRequestFormJSON(BaseModel):
    email: str
    password: str 