from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models
import bcrypt


def test_submit_fuelquote_form(client: TestClient, db_session: Session):
    # testing fuel quote submit
    queen = models.UserCredentials(
        id=0,
        username="cairo",
        password=bcrypt.hashpw(
            "Super Secret Please Encode This".encode("utf-8"), bcrypt.gensalt()
        ),
    )
    db_session.add(queen)
    db_session.commit()
    profile = models.ClientInformation(
        userid=0,
        full_name="Cairo A",
        address_1="123 Test Street",
        address_2="Moody Towers",
        city="Houston",
        state="TX",
        zipcode=77001,
    )
    db_session.add(profile)
    db_session.commit()
    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "cairo",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
            "suggested_price": 2,
            "total_amount_due": 1200,
        },
        cookies={"username": "cairo"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "cairo",
        "gallons_requested": 500,
        "delivery_address": "123 Test Street",
        "delivery_date": "2023-08-01",
        "suggested_price": 2,
        "total_amount_due": 1200,
    }
    # testing errror for if user hasnt created profile yet
    rat = models.UserCredentials(
        id=1,
        username="rat",
        password=bcrypt.hashpw(
            "Super Secret Please Encode This".encode("utf-8"), bcrypt.gensalt()
        ),
    )
    db_session.add(rat)
    db_session.commit()

    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "rat",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
            "suggested_price": 2,
            "total_amount_due": 1200,
        },
        cookies={"username": "rat"},
    )
    assert response.status_code == 403

    # testing error for missing fields
    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "cairo",
            "gallons_requested": 500,
            "delivery_date": "2023-08-01",
            "suggested_price": 2,
            "total_amount_due": 1200,
        },
        cookies={"username": "cairo"},
    )
    assert response.status_code == 422

    # testing error if user doesnt have account yet
    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "lanisdeodarant",
            "gallons_requested": 500,
            "delivery_address": "nowhere st",
            "delivery_date": "2023-08-01",
            "suggested_price": 2,
            "total_amount_due": 1200,
        },
        cookies={"username": "lanisdeodorant"},
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Username does not exist"}


def test_get_fuelquotes_by_user(client: TestClient, db_session: Session):

    queen = models.UserCredentials(
        id=0,
        username="Cairo",
        password=bcrypt.hashpw(
            "Super Secret Please Encode This".encode("utf-8"), bcrypt.gensalt()
        ),
    )
    db_session.add(queen)
    db_session.commit()
    fuelquote = models.FuelQuote(
        id=0,
        username="Cairo",
        gallons_requested=1000,
        delivery_address="123 Test Street",
        delivery_date="2023-07-31",
        suggested_price=2,
        total_amount_due=2500,
    )
    db_session.add(fuelquote)
    db_session.commit()
    response = client.get("/api/fuel_quote/Cairo", cookies={"username": "Cairo"})
    assert response.status_code == 200
    assert response.json() == [
        {
            "username": "Cairo",
            "gallons_requested": 1000,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-07-31",
            "suggested_price": 2,
            "total_amount_due": 2500,
        }
    ]
