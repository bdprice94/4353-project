from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, exc
from sqlalchemy.exc import IntegrityError

import app.schemas as schemas
import app.models as models
from app.api import deps

import bcrypt

router = APIRouter()


def contains_special_char(password):
    valid_chars = "!@#$%^&*()<>,.;:'[]{}=-0987654321"
    for char in password:
        if char in valid_chars:
            return True
    return False


@router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: schemas.UserCreate, db: Session = Depends(deps.get_session)
):
    if (
        len(user.password) < 8
        or user.password != user.password2
        or not contains_special_char(user.password)
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please ensure that the password is at least 8 characters, "
            + "that the passwords match, and that the password contains a special "
            + "character",
        )
    hash_pass = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    user = models.UserCredentials(
        username=user.username, password=hash_pass
    )
    try:
        db.add(user)
        db.commit()
    except IntegrityError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Username already exists",
        )

    return {"username": user.username}


@router.get("/", response_model=List[schemas.User])
async def get_users(db: Session = Depends(deps.get_session)):
    users = db.query(models.UserCredentials).all()
    return users


@router.post("/login", response_model=schemas.User)
async def login(user: schemas.UserLogin, db: Session = Depends(deps.get_session)):
    user_m = models.UserCredentials
    user_data = db.query(user_m).where(
        user_m.username == user.username).first()
    if not user_data or not bcrypt.checkpw(
        user.password.encode("utf-8"), user_data.password.encode("utf-8")
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password",
        )
    return {"id": user_data.id, "username": user_data.username}
