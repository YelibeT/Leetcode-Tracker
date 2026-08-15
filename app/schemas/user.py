from pydantic import BaseModel

class UserCreate(BaseModel):
    telegram_id: int
    leetcode_username: str
    mode: str
    roadmap: str | None = None