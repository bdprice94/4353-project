from typing import List

from fastapi import APIRouter, Depends, HTTPException, status,Query
from sqlalchemy.orm import Session, exc
from sqlalchemy.exc import IntegrityError

import app.schemas as schemas
import app.models as models
from app.api import deps

router = APIRouter()


@router.post("/user_profile/{username}", response_model=schemas.UserProfile)
async def update_profile(username: str, profile: schemas.UserProfile, db: Session = Depends(deps.get_session)):
    if (len(str(profile.zipcode)) > 9 or len(str(profile.zipcode)) < 5):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="please enter a valid zipcode")
    user = db.query(models.UserCredentials).filter(models.UserCredentials.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    clientInfo = models.ClientInformation(
        userid=user.id,
        full_name=profile.full_name,
        address_1=profile.address_1,
        address_2=profile.address_2,
        city=profile.city,
        state=profile.state,
        zipcode=profile.zipcode,
    )
    db.add(clientInfo)
    db.commit()
    return {"username": user.username,
            "full_name": clientInfo.full_name,
            "address_1": clientInfo.address_1,
            "address_2": clientInfo.address_2,
            "city": clientInfo.city,
            "state": clientInfo.state,
            "zipcode": clientInfo.zipcode
            }


@router.get("/profile/{username}", response_model=schemas.UserProfile)
async def get_profile_details_by_username(username: str, db: Session = Depends(deps.get_session)):
    userid = db.query(models.UserCredentials.id).filter(models.UserCredentials.username == username).scalar()
    if not userid:
        raise HTTPException(status_code=404, detail="User not found")
    clientInfo = db.query(models.ClientInformation).filter(models.ClientInformation.userid == userid).first()
    if not clientInfo:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": username,
            "full_name": clientInfo.full_name,
            "address_1": clientInfo.address_1,
            "address_2": clientInfo.address_2,
            "city": clientInfo.city,
            "state": clientInfo.state,
            "zipcode": clientInfo.zipcode
            }
