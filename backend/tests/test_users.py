from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models
import bcrypt


def test_get_users(client: TestClient, db_session: Session):
    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 0

    professor = models.UserCredentials(
        id=0,
        username="Professor Singh",
        password="Super Secret Please Encode This".encode("utf-8"),
    )
    db_session.add(professor)
    db_session.commit()

    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 1
    assert users[0]["username"] == "Professor Singh"


def test_add_user(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "Cat12356!", "password2": "Cat12356!"},
    )

    assert response.status_code == 201

    user = (
        db_session.query(models.UserCredentials)
        .where(models.UserCredentials.username == "Cat")
        .first()
    )
    assert user is not None
    assert user.username == "Cat"


def test_login(client: TestClient, db_session: Session):
    professor = models.UserCredentials(
        id=0,
        username="Professor Singh",
        password=str(
            bcrypt.hashpw(
                "Super Secret Please Encode This".encode("utf-8"), bcrypt.gensalt()
            ),
            "utf-8",
        ),
    )
    db_session.add(professor)
    db_session.commit()

    response = client.post(
        "/api/users/login",
        json={
            "username": "Professor Singh",
            "password": "Super Secret Please Encode This",
        },
    )

    contents = response.json()
    assert response.status_code == 200
    assert contents["id"] == 0
    assert contents["username"] == "Professor Singh"


# Regression test to ensure backend works purely from API calls for registration->login cycle
def test_user_full_circle(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "Cat12356!", "password2": "Cat12356!"},
    )

    assert response.status_code == 201

    response = client.post(
        "/api/users/login",
        json={
            "username": "Cat",
            "password": "Cat12356!",
        },
    )

    contents = response.json()
    assert response.status_code == 200
    assert contents["username"] == "Cat"


def test_taken_username(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "Cat12356!", "password2": "Cat12356!"},
    )
    assert response.status_code == 201

    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "Cat12356!", "password2": "Cat12356!"},
    )
    assert response.status_code == 422
    assert response.json()["detail"] == "Username already exists"


def test_invalid_password(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={
            "username": "Cat",
            "password": "Pneumonoultramicroscopicsilicovolcanoconiosis",
            "password2": "Pneumonoultramicroscopicsilicovolcanoconiosis",
        },
    )

    assert response.status_code == 400


def test_short_password(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "t1256!", "password2": "t1256!"},
    )

    assert response.status_code == 400


def test_mismatched_password(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "Cat1234567", "password2": "Cat567"},
    )

    assert response.status_code == 400


def test_nonexistent_user(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/login", json={"username": "Cat", "password": "Cat1234567!"}
    )

    assert response.status_code == 404


def test_wrong_password(client: TestClient, db_session: Session):
    professor = models.UserCredentials(
        id=0,
        username="Professor Singh",
        password=str(
            bcrypt.hashpw(
                "Super Secret Please Encode This".encode("utf-8"), bcrypt.gensalt()
            ),
            "utf-8",
        ),
    )
    db_session.add(professor)
    db_session.commit()

    response = client.post(
        "/api/users/login",
        json={"username": "Professor Singh", "password": "Cat1234567!"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Incorrect username or password"


def test_no_username(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/login", json={"username": "", "password": "Cat1234567!"}
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Username must not be empty"


def test_no_password_login(client: TestClient, db_session: Session):
    response = client.post("/api/users/login", json={"username": "Cat", "password": ""})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Password must not be empty"


def test_no_password_create(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "", "password2": "Hiasoiddaod!!11"},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Password must not be empty"


def test_no_password2_create(client: TestClient, db_session: Session):
    response = client.post(
        "/api/users/create_user",
        json={"username": "Cat", "password": "Hiasoiddaod!!11", "password2": ""},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Password must not be empty"
