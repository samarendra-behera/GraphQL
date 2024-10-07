import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await db.create_all()
    yield
    # Shutdown logic
    await db.close()

def init_app():
    apps = FastAPI(
        title="Lorem Ipsum",
        description="Fast API",
        version="1.0.0",
        lifespan=lifespan
    )

    @apps.get('/')
    def home():
        return "Welcome to home!"

    
    return apps


app = init_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)