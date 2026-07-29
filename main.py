from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    telegram_id: int
    telegram_username: str
    leetcode_username: str

class ResponseUser(BaseModel):
    id:int
    telegram_id: int
    telegram_username: str
    leetcode_username: str
users=[]
@app.post("/users")
def users(user:User, response_model=list[ResponseUser]):
    ResponseUser.id=len(users)+1
    users.append(user)
    return user

@app.get("/users")
def get_users():
    return users

@app.get("/user/{id}")
def get_user(id: int):
    return users[id]

@app.put("/users/{index}")
def update(index:int, user:User):
    users[index]=user
    return users
