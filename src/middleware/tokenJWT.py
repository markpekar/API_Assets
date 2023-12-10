import datetime
from fastapi import Depends, HTTPException,status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from ..auth.database import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generateJWT(userId):
    expire = datetime.utcnow() + timedelta(days=5)
    tokenData = {"userId":userId, "exp":expire.isoformat()}
    return jwt.encode(tokenData,"secret", algorithm='HS256')

def validateJWT(token):
    try:
        payload = jwt.decode(token, "secret", algorithm='HS256')
        userId: str = payload.get("userId")
        if userId is None:
            raise  HTTPException(400,"Auth failed")
        if datetime(payload.get("exp")) > datetime.utcnow():
            raise HTTPException(400,"token expired")
    except JWTError:
        return False

    return userId
    
async def get_current_user(token: str):
    userId = validateJWT(token)
    if(not userId):
        return HTTPException(400,"Auth failed")
    
    user = usersDB.find_one({ "_id": userId})
    if user is None:
        return HTTPException(400,"Auth failed")

    return user
