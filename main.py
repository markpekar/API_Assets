import uvicorn
from fastapi import FastAPI
from src.auth.routes import router as authRouter
from config.database import get_database
from src.posts.routes import router as postRouter

app = FastAPI()

app.include_router(authRouter)  
app.include_router(postRouter)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
    