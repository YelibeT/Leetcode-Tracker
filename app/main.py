from fastapi import FastAPI
from app.routers.users import users_router


app = FastAPI(title="LeetTracker API")
app.include_router(users_router)

@app.get("/")

def root():
    return {"message": "Welcome to LeetTracker API"}