from ..utils.password import get_password_hash, verify_password
from fastapi.encoders import jsonable_encoder
from .database import *
from fastapi.responses import Response
from ..middleware.tokenJWT import generateJWT, validateJWT
 

class UserManager:
    async def createUser(userData):
        hashed_password = get_password_hash(str(userData.password))
        if(usersDB.find_one({"email":userData.email}) != None):
            return Response("User already exist", 400)

        userData.password = hashed_password
        usersDB.insert_one(jsonable_encoder(userData))
        
        return Response("User created", 201)

    async def authUser(userData):
        plainPassword = userData.password
        res = usersDB.find_one(jsonable_encoder({"email":userData.email}))

        if(not verify_password(plainPassword,res["password"])):
            return Response("Wrong password", 403)
        
        token = generateJWT(str(res["_id"]))

        return Response(jsonable_encoder(token),200)

        
         
        