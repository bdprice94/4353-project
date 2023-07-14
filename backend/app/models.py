from sqlalchemy import Column, Integer, String,Date,ForeignKey
from sqlalchemy.orm import relationship
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

    fuel_quotes = relationship("FuelQuote", back_populates="user")
  
class FuelQuote(Base):
    __tablename__ = "fuelquote"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"))
    gallons_requested = Column(Integer)
    delivery_address = Column(String)
    delivery_date = Column(Date)
    suggested_price = Column(Integer)
    total_amount_due = Column(Integer)

    user = relationship("User", back_populates="fuel_quotes")