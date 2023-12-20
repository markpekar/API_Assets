import datetime
from bson import ObjectId
from jose import ExpiredSignatureError, JWTError, jwt
from datetime import datetime, timedelta
from ..auth.database import *
from fastapi.responses import JSONResponse
from decouple import config

tokenKey = config("SECRET")

def generateJWT(userId):
    expire = datetime.utcnow() + timedelta(days=5)
    tokenData = {"userId":userId, "exp":expire}
    return jwt.encode(tokenData,tokenKey, algorithm='HS256')

def validateJWT(token):
    try:
        payload = jwt.decode(token, tokenKey, algorithms='HS256')
        userId = payload.get("userId")
        
        res = usersDB.find({"_id":ObjectId(userId)})
        email = list(res)[0]["email"]
    
    except ExpiredSignatureError:
        return JSONResponse({"message":"Token expired. Please relogin"}, 403)

    except JWTError:
        return JSONResponse({"message":"Token is invalid"}, 403)

    return JSONResponse({"userId":userId, "email": email}, 200)
    
