from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    address_1 = Column(String)
    address_2 = Column(String,nullable=True)
    city = Column(String)
    state = Column(String)
    zipcode = Column(Integer)
