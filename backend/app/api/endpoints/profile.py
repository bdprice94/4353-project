from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models
from app.api import deps

router = APIRouter()


@router.post("/{username}", response_model=schemas.UserProfile)
async def update_profile(
    profile: schemas.UserProfile,
    user_credentials: models.UserCredentials = Depends(
        deps.get_user_credentials),
    db: Session = Depends(deps.get_session),
):
    if len(str(profile.zipcode)) > 9 or len(str(profile.zipcode)) < 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="please enter a valid zipcode",
        )

    client_information = models.ClientInformation(
        userid=user_credentials.id,
        full_name=profile.full_name,
        address_1=profile.address_1,
        address_2=profile.address_2,
        city=profile.city,
        state=profile.state,
        zipcode=profile.zipcode,
    )
    db.add(client_information)
    db.commit()

    user_profile = schemas.UserProfile(
        username=user_credentials.username,
        full_name=client_information.full_name,
        address_1=client_information.address_1,
        address_2=client_information.address_2,
        city=client_information.city,
        state=client_information.state,
        zipcode=client_information.zipcode
    )
    return user_profile


@router.get("/{username}", response_model=schemas.UserProfile)
async def get_profile_details_by_username(
    user_credentials: models.UserCredentials = Depends(
        deps.get_user_credentials),
    client_information: models.ClientInformation = Depends(
        deps.get_client_information),
):
    user_profile = schemas.UserProfile(
        username=user_credentials.username,
        full_name=client_information.full_name,
        address_1=client_information.address_1,
        address_2=client_information.address_2,
        city=client_information.city,
        state=client_information.state,
        zipcode=client_information.zipcode
    )
    return user_profile
