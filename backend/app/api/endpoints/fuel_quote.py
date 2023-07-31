from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.FuelQuote)
async def submit_fuelquote_form(
    fuel_quote: schemas.FuelQuote,
    user_credentials: models.UserCredentials = Depends(
        deps.get_user_credentials),
    client_information: models.ClientInformation = Depends(
        deps.get_client_information),
    db: Session = Depends(deps.get_session),
):
    fuel_quote_model = models.FuelQuote(
        username=fuel_quote.username,
        gallons_requested=fuel_quote.gallons_requested,
        delivery_address=fuel_quote.delivery_address,
        delivery_date=fuel_quote.delivery_date,
        suggested_price=fuel_quote.suggested_price,
        total_amount_due=fuel_quote.total_amount_due,
    )
    db.add(fuel_quote_model)
    db.commit()
    return fuel_quote


@router.get("/{username}", response_model=List[schemas.FuelQuote])
async def get_fuelquotes(
    user_credentials: models.UserCredentials = Depends(
        deps.get_user_credentials),
    db: Session = Depends(deps.get_session),
):
    fuel_quotes = (
        db.query(models.FuelQuote)
        .filter(models.FuelQuote.username == user_credentials.username)
        .all()
    )
    return fuel_quotes


@router.post("/price")
def get_fuel_price(
    fuel_quote: schemas.FuelQuote,
    user_credentials: models.UserCredentials = Depends(
        deps.get_user_credentials),
    client_information: models.ClientInformation = Depends(
        deps.get_client_information),
    db: Session = Depends(deps.get_session),
) -> int:
    base_price = 1.5

    if client_information.state == "TX":
        base_price += .02
    else:
        base_price += .04

    user_history = db.query(models.FuelQuote).where(
        models.FuelQuote.username == user_credentials.username)
    if user_history:
        base_price -= .01

    if fuel_quote.gallons_requested > 1000:
        base_price += .02
    else:
        base_price += .03

    # Company profits. We are told to always add this.
    base_price += .1

    return base_price * fuel_quote.gallons_requested
