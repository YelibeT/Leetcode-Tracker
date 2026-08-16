import sqlite3

connection = sqlite3.connect("leetcode_tracker.db")
cursor = connection.cursor()

cursor.execute(
    "ALTER TABLE users ADD COLUMN mode TEXT"
)

cursor.execute(
    "ALTER TABLE users ADD COLUMN roadmap TEXT"
)

connection.commit()
connection.close()

print("Database updated successfully!")