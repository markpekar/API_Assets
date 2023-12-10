import uvicorn
from fastapi import FastAPI
from src.auth.routes import router as authRouter
from config.database import get_database

app = FastAPI()

app.include_router(authRouter);  

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
    get_database()
    