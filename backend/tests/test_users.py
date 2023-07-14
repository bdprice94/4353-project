from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models

def test_endpoint(client: TestClient, db_session: Session):
    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 0

    professor = models.User(
        id = 0,
        username = "Professor Singh",
        password = "Super Secret Please Encode This",
        full_name = "Dr. Raj Singh",
        address_1 = "University",
        address_2 = "Planet Earth",
        city = "London",
        state = "Peace",
        zipcode = "1234"
    )
    db_session.add(professor)
    db_session.commit()

    response = client.get("/api/users")
    users = response.json()
    assert response.status_code == 200
    assert len(users) == 1
    assert users[0]['username'] == "Professor Singh"
    