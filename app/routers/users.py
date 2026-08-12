from fastapi import APIRouter, Depends
from sqlalchemy.orm import session

from app.databse.db import get_db
from app.databse.models import User
from app.schemas.user import UserCreate

users_router=APIRouter()

@users_router.post("/users")
def create_user(
    user:UserCreate,
    db:Session=Depends(get_db)
):
    new_user=User(
        telegram_id=user.telegram_id,
        leetcode_username=user.leetcode_username
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user