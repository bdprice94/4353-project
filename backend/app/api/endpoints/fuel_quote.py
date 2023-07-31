from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from app.api import deps

router = APIRouter()


def calculate_suggested_price(
    client_information: models.ClientInformation,
    user_credentials: models.UserCredentials,
    db: Session,
    fuel_quote: schemas.FuelQuote,
):
    if fuel_quote.gallons_requested < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Your fuel quote must be 1 gallon or more",
        )

    if client_information.state is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Your profile must have a state setup",
        )

    base_price = 1.5

    if client_information.state == "TX":
        base_price += 0.02
    else:
        base_price += 0.04

    user_history = db.query(models.FuelQuote).where(
        models.FuelQuote.username == user_credentials.username
    )
    if user_history:
        base_price -= 0.01

    if fuel_quote.gallons_requested > 1000:
        base_price += 0.02
    else:
        base_price += 0.03

    # Company profits. We are told to always add this.
    base_price += 0.1
    return base_price


@router.post("/", response_model=schemas.FuelQuote)
async def submit_fuelquote_form(
    fuel_quote: schemas.FuelQuote,
    user_credentials: models.UserCredentials = Depends(
        deps.get_user_credentials),
    client_information: models.ClientInformation = Depends(
        deps.get_client_information),
    db: Session = Depends(deps.get_session),
):
    suggested_price = calculate_suggested_price(
        client_information, user_credentials, db, fuel_quote
    )

    fuel_quote_model = models.FuelQuote(
        username=fuel_quote.username,
        gallons_requested=fuel_quote.gallons_requested,
        delivery_address=fuel_quote.delivery_address,
        delivery_date=fuel_quote.delivery_date,
        suggested_price=suggested_price,
        total_amount_due=suggested_price * fuel_quote.gallons_requested,
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
):
    suggested_price = calculate_suggested_price(
        client_information, user_credentials, db, fuel_quote
    )

    return {
        'total_price': suggested_price * fuel_quote.gallons_requested,
        'price_per_gallon': suggested_price
    }
