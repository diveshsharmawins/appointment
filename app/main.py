from fastapi import FastAPI
from app.api import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "FastAPI with PostgreSQL"}
