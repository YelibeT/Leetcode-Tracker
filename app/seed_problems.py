import csv

from app.databse.db import SessionLocal
from app.databse.models import Problem


def seed_problems():
    db = SessionLocal()

    try:
        with open("data/problems.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                problem = Problem(
                    title=row["title"],
                    slug=row["slug"],
                    difficulty=row["difficulty"],
                    category=row["category"],
                    roadmap=row["roadmap"],
                    position=int(row["position"])
                )

                db.add(problem)

        db.commit()

        print("Problems seeded successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding problems: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_problems()