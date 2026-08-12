from fastapi import APIRouter, Depends, HTTPException
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
    existing_user = db.query(User).filter(
            User.telegram_id == user.telegram_id
        ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User is already registered"
        )
    
    new_user=User(
        telegram_id=user.telegram_id,
        leetcode_username=user.leetcode_username
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@users_router.get("/users/{telegram_id}")
def get_user(
    telegram_id:int,
    db:Session=Depends(get_db)
):
    user=db.query(User).filter(
        User.telegram_id==telegram_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user