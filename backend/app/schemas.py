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
    id = int 
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

class UserProfile(User):
    id: Optional[int] = None # if youre wondering why I did this its because since UserProfile inherits from User, I made it optional in userprofile so when a form is submitted the id will not be changed and id will not prevent the form from submitting, btw it was the only way i could get both form and display to work so if you have any suggestions let me know slay
    full_name:str
    address_1: str
    address_2:Optional[str] |  'None'
    city: str
    state: str
    zipcode: int
    