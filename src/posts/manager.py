import json
from ..utils.parser import parse_json
from ..posts.schemas import Post
from .database import *
from fastapi.responses import JSONResponse
from bson import ObjectId
from ..auth.database import *

 
class PostManager:
    async def getAllPosts():
        res = postsDB.find()
        return JSONResponse(parse_json(res), 200)
    
    async def createPost(post:Post, userData):
        currentUserData = json.loads(userData.decode())
        userId = currentUserData["userId"]
        
        post = dict(post)
        post["creatorId"] = userId
        postsDB.insert_one(parse_json(post))
        return JSONResponse("Post created", 201)    
        
    async def getPostById(id): 
        res = postsDB.find({"_id":ObjectId(id)})
        return JSONResponse(parse_json(res), 200)