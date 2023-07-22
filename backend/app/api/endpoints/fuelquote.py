
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from app.api import deps

router = APIRouter()


@router.post("/fuelquote/{username}", response_model=schemas.FuelQuote)
async def submit_fuelquote_form(fuelquote: schemas.FuelQuote, user_credentials: models.UserCredentials = Depends(deps.get_user_credentials), client_information: models.ClientInformation = Depends(deps.get_client_information), db: Session = Depends(deps.get_session)):
    fuelquote = models.FuelQuote(
        username=user_credentials.username,
        gallons_requested=fuelquote.gallons_requested,
        delivery_address=fuelquote.delivery_address,
        delivery_date=fuelquote.delivery_date,
        suggested_price=fuelquote.suggested_price,
        total_amount_due=fuelquote.total_amount_due
    )
    db.add(fuelquote)
    db.commit()
    return {"username": user_credentials.username,
            "gallons_requested": fuelquote.gallons_requested,
            "delivery_address": fuelquote.delivery_address,
            "delivery_date": fuelquote.delivery_date,
            "suggested_price": fuelquote.suggested_price,
            "total_amount_due": fuelquote.total_amount_due
            }


@router.get("/getfuelquote/{username}", response_model=List[schemas.FuelQuote])
async def get_fuelquotes_by_user(user_credentials: models.UserCredentials = Depends(deps.get_user_credentials), db: Session = Depends(deps.get_session)):
    fuelquote = db.query(models.FuelQuote).filter(
        models.FuelQuote.username == user_credentials.username).all()
    return fuelquote
