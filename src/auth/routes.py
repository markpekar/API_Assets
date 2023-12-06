from fastapi import APIRouter
from .manager import UserManager

router = APIRouter(
    prefix="/auth",
)

@router.get("/signup")
async def createUser():   
        return await UserManager.createUser("ads","dasdas")