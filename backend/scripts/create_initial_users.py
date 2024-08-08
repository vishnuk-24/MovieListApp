import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import SessionLocal, create_user
from sqlalchemy.orm import Session


def create_initial_users():
    db = SessionLocal()
    try:
        create_user(db, "admin", "adminpassword")
        create_user(db, "testuser1", "testpassword1")
        create_user(db, "testuser2", "testpassword2")
        print("Initial users created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    create_initial_users()
