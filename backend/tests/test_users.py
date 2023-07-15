from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def test_get_users(client: TestClient, db_session: Session):
    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 0

    professor = models.User(
        id=0,
        username="Professor Singh",
        password="Super Secret Please Encode This",
        full_name="Dr. Raj Singh",
        address_1="University",
        address_2="Planet Earth",
        city="London",
        state="Peace",
        zipcode="1234"
    )
    db_session.add(professor)
    db_session.commit()

    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 1
    assert users[0]['username'] == "Professor Singh"


def test_add_user(client: TestClient, db_session: Session):
    response = client.post("/api/users/create_user", json={
        "username": "Cat",
        "password": "Cat12356!",
        "password2": "Cat12356!"
    })

    assert response.status_code == 201

    user = db_session.query(models.User).where(
        models.User.username == "Cat").first()
    assert user is not None
    assert user.username == "Cat"


def test_login(client: TestClient, db_session: Session):
    professor = models.User(
        id=0,
        username="Professor Singh",
        password="Super Secret Please Encode This",
        full_name="Dr. Raj Singh",
        address_1="University",
        address_2="Planet Earth",
        city="London",
        state="Peace",
        zipcode="1234"
    )
    db_session.add(professor)
    db_session.commit()

    response = client.post("/api/users/login", json={
        "username": "Professor Singh",
        "password": "Super Secret Please Encode This"
    })

    contents = response.json()
    assert response.status_code == 200
    assert contents["id"] == 0
    assert contents["username"] == "Professor Singh"
