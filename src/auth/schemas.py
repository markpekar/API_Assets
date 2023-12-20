from pydantic import BaseModel

class User(BaseModel):
    email : str
    password: str

class TokenSchema(BaseModel):
    token: str
    

