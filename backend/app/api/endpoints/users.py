from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models
from app.api import deps

router = APIRouter()


@router.post("/create_db_table")
async def create_user_table(db: Session = Depends(deps.get_session)):
    # To be replaced by Alembic
    query = "CREATE TABLE users (id SERIAL PRIMARY KEY, email varchar(255), password varchar(255))"
    db.execute(text(query))
    db.commit()

    return "Table is created. We should not create database tables like this. Please get a proper tool for migrations."


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_session)):
    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()

    return user


@router.get("/", response_model=List[schemas.User])
async def get_users(db: Session = Depends(deps.get_session)):
    users = db.query(models.User).all()
    return users