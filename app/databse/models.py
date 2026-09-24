from sqlalchemy import Column, Integer, String
from app.databse.db import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    telegram_id=Column(Integer, unique=True)
    leetcode_username=Column(String, nullable=False)
    mode= Column(String, nullable=True)
    roadmap= Column(String, nullable=True)
    current_position = Column(Integer, default=1)

class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    category = Column(String, nullable=False)
    roadmap = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
