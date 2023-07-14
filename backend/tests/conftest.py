import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from app.app import app
from app.api.deps import get_session
from app.database import Base


@pytest.fixture(scope="session")
def db_engine() -> Engine:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db_session(db_engine: Engine) -> Session:
    connection = db_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    try:
        yield session
    finally:
        # This is important, as after each test our DB will be blank once again.
        # We can test all combinations of data imaginable like this.
        transaction.rollback()
        session.close()


@pytest.fixture
def client(db_session: Session):
    def get_session_override():
        return db_session

    app.dependency_overrides[get_session] = get_session_override
    # When we usually call an endpoint we get a database connection yielded
    # to us via deps.py; Since we are straight up using our app here to test it,
    # one issue it will run into is generating that db connection when needed.
    # That is because we do not run postgres during unit testing.
    # The code above is responsible for intercepting the DB code and giving our app
    # a fake database, that will be only used for this test.

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
