from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date,datetime
import app.models as models
import app.schemas as schemas
from app.api import deps

router = APIRouter()


@router.post("/fuelquote/{username}",  response_model=schemas.FuelQuote)
async def submit_fuelquote_form(username:str,fuelquote: schemas.FuelQuote, db: Session = Depends(deps.get_session)
):

  user = db.query(models.User).where(models.User.username == fuelquote.username)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


  fuelquote = models.FuelQuote(username= username, gallons_requested= fuelquote.gallons_requested,delivery_address = fuelquote.delivery_address,delivery_date=fuelquote.delivery_date,suggested_price = fuelquote.suggested_price,total_amount_due = fuelquote.total_amount_due)
  db.add(fuelquote)
  db.commit()
  
  return {"username": username, "gallons_requested":fuelquote.gallons_requested, "delivery_address":fuelquote.delivery_address, "delivery_date":fuelquote.delivery_date, "suggested_price": fuelquote.suggested_price, "total_amount_due":fuelquote.total_amount_due}
 