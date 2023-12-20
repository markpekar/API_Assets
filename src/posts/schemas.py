from pydantic import BaseModel

class Post(BaseModel):
    name: str
    formats: list
    createdIn: str
    fileSize: float
    polyCount: int
    description: str
    price: float