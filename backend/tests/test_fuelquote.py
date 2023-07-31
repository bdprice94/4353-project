from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models
import bcrypt


def add_fake_user(db_session: Session):
    user = models.UserCredentials(
        id=0,
        username="RegularUser",
        password=bcrypt.hashpw(
            "Super Secret Please Encode This".encode("utf-8"), bcrypt.gensalt()
        ),
    )
    db_session.add(user)
    db_session.commit()


def add_fake_client_info(db_session: Session):
    profile = models.ClientInformation(
        userid=0,
        full_name="Regular Username",
        address_1="123 Test Street",
        address_2="Moody Towers",
        city="Houston",
        state="TX",
        zipcode=77001,
    )
    db_session.add(profile)
    db_session.commit()


def add_fake_quote(db_session: Session):
    fuelquote = models.FuelQuote(
        id=0,
        username="RegularUser",
        gallons_requested=1000,
        delivery_address="123 Test Street",
        delivery_date="2023-07-31",
        suggested_price=2,
        total_amount_due=2000,
    )
    db_session.add(fuelquote)
    db_session.commit()


def test_submit_form(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    add_fake_client_info(db_session)

    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "RegularUser",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "RegularUser"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "RegularUser",
        "gallons_requested": 500,
        "delivery_address": "123 Test Street",
        "delivery_date": "2023-08-01",
    }


def test_form_no_profile(client: TestClient, db_session: Session):
    add_fake_user(db_session)

    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "RegularUser",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "RegularUser"},
    )
    assert response.status_code == 403


def test_missing_fields(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    add_fake_client_info(db_session)

    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "RegularUser",
            "gallons_requested": 500,
            "delivery_date": "2023-08-01",
            # Missing delivery address
        },
        cookies={"username": "RegularUser"},
    )
    assert response.status_code == 422


def test_user_does_not_exist(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    add_fake_client_info(db_session)

    response = client.post(
        "/api/fuel_quote/",
        json={
            "username": "DoesNotExist",
            "gallons_requested": 500,
            "delivery_address": "nowhere st",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "DoesNotExist"},
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Username does not exist"}


def test_get_fuelquote(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    add_fake_client_info(db_session)
    add_fake_quote(db_session)

    response = client.get(
        "/api/fuel_quote/RegularUser", cookies={"username": "RegularUser"}
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "username": "RegularUser",
            "gallons_requested": 1000,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-07-31",
            "suggested_price": 2,
            "total_amount_due": 2000,
        }
    ]


def test_get_price(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    add_fake_client_info(db_session)
    response = client.post(
        "/api/fuel_quote/price",
        json={
            "username": "RegularUser",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "RegularUser"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "username": "RegularUser",
        "gallons_requested": 500,
        "delivery_address": "123 Test Street",
        "delivery_date": "2023-08-01",
        "suggested_price": 1.6400000000000001,
        "total_amount_due": 820.0000000000001,
    }
    # Price is 820


def test_get_price_no_profile(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    response = client.post(
        "/api/fuel_quote/price",
        json={
            "username": "RegularUser",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "RegularUser"},
    )

    assert response.status_code == 403


def test_get_price_invalid_user(client: TestClient, db_session: Session):
    response = client.post(
        "/api/fuel_quote/price",
        json={
            "username": "RegularUser",
            "gallons_requested": 500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "RegularUser"},
    )

    assert response.status_code == 403


def test_get_price_invalid_form(client: TestClient, db_session: Session):
    add_fake_user(db_session)
    add_fake_client_info(db_session)

    response = client.post(
        "/api/fuel_quote/price",
        json={
            "username": "RegularUser",
            "gallons_requested": -500,
            "delivery_address": "123 Test Street",
            "delivery_date": "2023-08-01",
        },
        cookies={"username": "RegularUser"},
    )
    assert response.status_code == 400
