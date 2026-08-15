from sqlalchemy import Column, Integer, String
from app.databse.db import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    telegram_id=Column(Integer, unique=True)
    leetcode_username=Column(String, nullable=False)
    tracking_mode = Column(String, nullable=True)
    roadmap = Column(String, nullable=True)