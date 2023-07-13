from typing import List

from fastapi import APIRouter, Depends, HTTPException, status,Query
from sqlalchemy.orm import Session, exc
from sqlalchemy.exc import IntegrityError

import app.schemas as schemas
import app.models as models
from app.api import deps

router = APIRouter()


@router.post("/user_profile/{username}",  response_model=schemas.UserProfile, response_model_exclude={"id"})
async def update_profile(username:str,profile: schemas.UserProfile, db: Session = Depends(deps.get_session)):
  print(f"Received username: {username}") 
  user = db.query(models.User).filter(models.User.username == username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  user.username = username
  user.full_name = profile.full_name
  user.address_1 = profile.address_1
  user.address_2 = profile.address_2
  user.city = profile.city
  user.state = profile.state
  user.zipcode = profile.zipcode
  db.commit()
  return {"username":user.username,"full_name": user.full_name, "address_1": user.address_1, "address_2": user.address_2, "city": user.city, "state": user.state, "zipcode": user.zipcode}

@router.get("/profile/{username}", response_model=schemas.UserProfile)
async def get_profile_details_by_username(username: str, db: Session = Depends(deps.get_session)):
    
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user