from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

database_url = 'postgresql://localhost/postgres'

Base = declarative_base()
engine = create_engine(database_url)
if not database_exists(database_url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, bind=engine)
