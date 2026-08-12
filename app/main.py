from fastapi import FastAPI
from app.routers.users import users_router
from app.databse.db import engine, Base
from app.databse import models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router)

@app.get("/")

def root():
    return {"message": "Welcome to LeetTracker API"}