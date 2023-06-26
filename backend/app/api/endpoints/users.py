from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api import deps

router = APIRouter()


@router.post("/create_user_table")
async def create_user_table(db: Session = Depends(deps.get_session)):
    query = "CREATE TABLE users (id int, name varchar(255))"
    db.execute(text(query))
    db.commit()

    return "Done"


@router.post("/create_user")
async def create_user(username: str, db: Session = Depends(deps.get_session)):
    query = text(f"INSERT INTO users (id, name) VALUES (0, '{username}')")
    db.execute(query)
    db.commit()

    return "Done inserting"


@router.get("/get_users")
async def get_users(db: Session = Depends(deps.get_session)):
    query = text(f"SELECT * FROM users")
    result = db.execute(query)
    users = result.fetchall()
    usernames = []
    for (id, user) in users:
        usernames.append(user)

    db.commit()

    return usernames
