from fastapi import Cookie, Depends, HTTPException, status
from fastapi.security import APIKeyCookie
from sqlalchemy.orm import Session
from typing import Generator, Annotated

from app.database import SessionLocal
from app.models import UserCredentials, ClientInformation

api_key = APIKeyCookie(name="username", auto_error=False)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_username(cookie: str | None = Cookie(default=None, alias='username')) -> str:
    # Yes, this means that our authentication is simply "does the user give us a cookie"
    # this is not secure, but here we could call our authentication methodologies to confirm
    # whether or not what's in the cookie is correct and trusted.
    # This is pseudosecurity, we will trust our users to never fake a cookie. :)
    print(cookie)
    if not cookie:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid authentication")
    return cookie


def get_user_credentials(username: str = Depends(get_username), db: Session = Depends(get_session)) -> UserCredentials:
    user_credentials = db.query(UserCredentials).where(
        UserCredentials.username == username).scalar()
    print(user_credentials)
    if not user_credentials:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Username does not exist")

    return user_credentials


def get_client_information(user_credentials: UserCredentials = Depends(get_user_credentials), db: Session = Depends(get_session)) -> ClientInformation:
    user_information = db.query(ClientInformation).where(
        ClientInformation.userid == user_credentials.id).scalar()
    if not user_information:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Client information does not exist")

    return user_information
