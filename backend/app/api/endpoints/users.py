from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models
from app.api import deps

router = APIRouter()


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
