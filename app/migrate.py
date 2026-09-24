from sqlalchemy import text

from app.databse.db import engine


with engine.connect() as connection:
    connection.execute(
        text(
            "ALTER TABLE users "
            "ADD COLUMN current_position INTEGER DEFAULT 1"
        )
    )

    connection.commit()

print("Database updated successfully!")
