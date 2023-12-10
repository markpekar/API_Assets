from fastapi import APIRouter
from .manager import UserManager
from fastapi import Request
from .schemas import User


router = APIRouter(
    prefix="/auth",
)

@router.post("/signup")
async def createUser(data:User):   
        return await UserManager.createUser(data)

@router.post("/login")
async def createUser(data:User):   
        return await UserManager.authUser(data)

@router.get("/me")
async def getUserInfo(data:str):
        return await UserManager.authUser(data)