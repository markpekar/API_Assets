from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from ..middleware.tokenJWT import validateJWT
from .manager import PostManager
from .schemas import Post


router = APIRouter(
    prefix="/posts",
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get-all")
async def get_posts(token: Annotated[str, Depends(oauth2_scheme)]):
        validation = validateJWT(token)
        if(validation.status_code != 200):
              return validation

        return await PostManager.getAllPosts()
@router.post("/create-post")
async def create_new_post(post:Post, token: Annotated[str, Depends(oauth2_scheme)]):
        validation = validateJWT(token)
        if(validation.status_code != 200):
              return validation
        
        return await PostManager.createPost(dict(post), validation.body)
@router.get("/get-post/{id}")
async def getPostById(id ,token: Annotated[str, Depends(oauth2_scheme)]):
        validation = validateJWT(token)
        if(validation.status_code != 200):
              return validation


        return await PostManager.getPostById(id)
