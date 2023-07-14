# In your api.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas
from app.api import deps

router = APIRouter()


@router.post("/fuelquote/{username}",  response_model=schemas.FuelQuote)
async def submit_fuelquote_form(
  username:str,
  
  fuelquote: schemas.FuelQuote,
  db: Session = Depends(deps.get_session)
):
  user = db.query(models.User).filter(models.User.username == username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  user.gallons_requested = fuelquote.gallons_requested
  user.delivery_address = fuelquote.delivery_address
  user.delivery_date = fuelquote.delivery_date
  user.suggested_price = fuelquote.suggested_price
  user.total_amount_due = fuelquote.total_amount_due
  db.commit()
  return {
    "username":user.username,
    "gallons_requested": user.gallons_requested,
    "delivery_address": user.delivery_address,
    "delivery_date": user.delivery_date,
    "suggested_price": user.suggested_price,
    "total_amount_due": user.total_amount_due
  }
