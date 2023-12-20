from ..utils.password import get_password_hash, verify_password
from fastapi.encoders import jsonable_encoder
from .database import *
from fastapi.responses import JSONResponse
from ..middleware.tokenJWT import generateJWT
from email_validator import EmailNotValidError, validate_email
 

class UserManager:
    async def createUser(userData):
        try:
            validate_email(userData.email)
            hashed_password = get_password_hash(str(userData.password))
            if(usersDB.find_one({"email":userData.email}) != None):
                return JSONResponse({"message": "User already exist"}, 400)

            userData.password = hashed_password
            usersDB.insert_one(jsonable_encoder(userData))
        
            return JSONResponse({"message": "User created"}, 201)
        except EmailNotValidError:
            return JSONResponse({"message": "Email is not valid"}, 400)

    async def authUser(userData):
        plainPassword = userData.password
        res = usersDB.find_one({"email":userData.email})

        if(res == None):
            return JSONResponse({"message": "Wrong email"}, 403)
 
        if(not verify_password(plainPassword,res["password"])):
            return JSONResponse({"message": "Wrong password"}, 403)
        
        token = generateJWT(str(res["_id"]))

        return JSONResponse({"token": token},200)

        
         
        