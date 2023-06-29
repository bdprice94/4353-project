from typing import List

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models
from app.api import deps

router = APIRouter()


@router.post("/create_user")
async def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_session)):
    user = models.User(username=user.username, password=user.password)
    db.add(user)
    db.commit()

    return Response()


@router.get("/", response_model=List[schemas.User])
async def get_users(db: Session = Depends(deps.get_session)):
    users = db.query(models.User).all()
    return users


@router.post("/login", response_model=schemas.User)
async def login(user: schemas.UserLogin, db: Session = Depends(deps.get_session)):
    user_m = models.User
    user_data = db.query(user_m)\
        .filter(user_m.username == user.username, user_m.password == user.password)\
        .all()[0]

    return user_data
