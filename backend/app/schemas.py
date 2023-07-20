from pydantic import BaseModel, validator
from typing import Optional
from datetime import date,datetime


class UserBase(BaseModel):
    username: str

    @validator('username')
    def username_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError('Username must not be empty')
        return v.title()


class UserLogin(UserBase):
    password: str

    @validator('password')
    def password_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError('Password must not be empty')
        return v.title()


class UserCreate(UserBase):
    password: str
    password2: str

    @validator('password', 'password2')
    def password_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError('Password must not be empty')
        return v.title()


class FuelQuote(BaseModel):
    id: int
    username: str
    gallons_requested: int
    delivery_address: str
    delivery_date: str
    suggested_price: int
    total_amount_due: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserProfile(UserBase):
    full_name: str
    address_1: str
    address_2: Optional[str] | 'None'
    city: str
    state: str
    zipcode: int
