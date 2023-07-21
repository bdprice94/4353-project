from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas

import bcrypt

def test_update_profile(client: TestClient, db_session: Session):
    professor = models.UserCredentials(
        id=0,
        username="Professorsingh",
        password=bcrypt.hashpw("Super Secret Please Encode This".encode('utf-8'), bcrypt.gensalt())
    )
    db_session.add(professor)
    db_session.commit()
    response = client.post(
        "/api/profile/user_profile/Professorsingh",
        json={
            "username": "Professorsingh",
            "full_name": "Raj Singh",
            "address_1": "123 cougar village dr ",
            "address_2": "The Lofts",
            "city": "Houston",
            "state": "TX",
            "zipcode": 77004
        }
    )
    assert response.status_code == 200 

    assert response.json() == {
        "username": "Professorsingh",
        "full_name": "Raj Singh",
        "address_1": "123 cougar village dr ",
        "address_2": "The Lofts",
        "city": "Houston",
        "state": "TX",
        "zipcode": 77004
    } 

def test_get_profile_details_by_username(client: TestClient, db_session: Session):
     professor = models.UserCredentials(
        id=1,
        username="Ella",
        password=bcrypt.hashpw("blah".encode('utf-8'), bcrypt.gensalt())
     )
     db_session.add(professor)
     db_session.commit()
     profile = models.ClientInformation(
        userid=professor.id,
        full_name="Ella Caradang",
        address_1="123 cougar village dr ",
        address_2="Moody Towers",
        city="Houston",
        state="TX",
        zipcode=77004
     )
     db_session.add(profile)
     db_session.commit()
     
     response = client.get("api/profile/profile/Ella")
     assert response.status_code == 200
     assert response.json() == {
        "username": "Ella",
        "full_name": "Ella Caradang",
        "address_1": "123 cougar village dr ", 
        "address_2": "Moody Towers", 
        "city": "Houston",
        "state": "TX",
        "zipcode": 77004
     }


