from pydantic import BaseModel, validator
from typing import Optional

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
    
class UserProfile(UserBase):
    full_name:str
    address_1: str
    address_2:Optional[str] 
    city: str
    state: str
    zipcode: int
class User(UserBase):
    id: int
    UserProfile: Optional[UserProfile]
    
    class Config:
        orm_mode = True
