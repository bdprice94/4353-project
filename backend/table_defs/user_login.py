from pydantic import BaseModel, validator


class UserLogin(BaseModel):
    username:  str
    password:  str

    @validator('username')
    def username_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError('Username must not be empty')
        return v.title()

    @validator('password')
    def password_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError('Password must not be empty')
        return v.title()


class UserLoginResponse(BaseModel):
    status: bool
    text: str
