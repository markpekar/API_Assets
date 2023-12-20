from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from ..middleware.tokenJWT import validateJWT
from .manager import UserManager
from .schemas import User, TokenSchema


router = APIRouter(
    prefix="/auth",
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/signup")
async def createUser(data:User):   
        return await UserManager.createUser(data)

@router.post("/login")
async def createUser(data: User):   
        return await UserManager.authUser(data) 

@router.get("/me")
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        return validateJWT(token)