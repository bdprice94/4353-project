from pydantic import BaseModel, validator


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


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
