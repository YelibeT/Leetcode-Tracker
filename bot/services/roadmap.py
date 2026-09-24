from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.databse.models import Problem


DATABASE_URL = "sqlite:///./leetcode_tracker.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def get_next_problem(roadmap: str, position: int):
    db = SessionLocal()

    try:
        problem = db.query(Problem).filter(
            Problem.roadmap == roadmap,
            Problem.position == position
        ).first()

        return problem

    finally:
        db.close()

