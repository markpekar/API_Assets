from ..utils.password import get_password_hash
from .schemas import UserCreate

class UserManager:
    async def createUser(self, user: UserCreate):
        get_password_hash
        #try: 
            #hashed_password = get_password_hash(str(user.password))
        return "nice"
        
        