from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import database_exists, create_database

database_url = 'postgresql://localhost/db'


def get_engine() -> Engine:
    engine = create_engine(database_url)
    if not database_exists(database_url):
        create_database(engine.url)
    return engine
