from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas
import bcrypt


def test_get_users(client: TestClient, db_session: Session):
    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 0

    professor = models.UserCredentials(
        id=0,
        username="Professor Singh",
        password="Super Secret Please Encode This".encode('utf-8'),
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

    user = db_session.query(models.UserCredentials).where(
        models.UserCredentials.username == "Cat").first()
    assert user is not None
    assert user.username == "Cat"


def test_login(client: TestClient, db_session: Session):
    professor = models.UserCredentials(
        id=0,
        username="Professor Singh",
        password=bcrypt.hashpw("Super Secret Please Encode This".encode('utf-8'), bcrypt.gensalt())
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
