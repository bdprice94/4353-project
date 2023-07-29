from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from app.database import Base


class UserCredentials(Base):
    __tablename__ = "usercredentials"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(LargeBinary)


class ClientInformation(Base):
    __tablename__ = "clientinformation"

    userid = Column(
        Integer, ForeignKey(UserCredentials.id), primary_key=True, index=True
    )
    full_name = Column(String)
    address_1 = Column(String)
    address_2 = Column(String, nullable=True)
    city = Column(String)
    state = Column(String)
    zipcode = Column(Integer)


class FuelQuote(Base):
    __tablename__ = "fuelquote"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, ForeignKey(UserCredentials.username))
    gallons_requested = Column(Integer)
    delivery_address = Column(String)
    delivery_date = Column(String)
    suggested_price = Column(Integer)
    total_amount_due = Column(Integer)
