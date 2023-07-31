from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, datetime


class UserBase(BaseModel):
    username: str

    @validator("username")
    def username_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError("Username must not be empty")
        return v


class UserLogin(UserBase):
    password: str

    @validator("password")
    def password_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError("Password must not be empty")
        return v


class UserCreate(UserBase):
    password: str
    password2: str

    @validator("password", "password2")
    def password_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError("Password must not be empty")
        return v


class FuelQuote(BaseModel):
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
    address_2: Optional[str] | "None"
    city: str
    state: str
    zipcode: int
    @validator("full_name", "address_1","city","state",each_item=True)
    def profile_must_not_be_empty(cls, v,field):
        if len(v) < 1:
            raise ValueError(f"Uh Oh! {field.name} must not be empty")
        return v
    