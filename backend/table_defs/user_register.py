from pydantic import BaseModel, validator


class UserRegister(BaseModel):
    username:  str
    password:  str
    password2: str

    @validator('username')
    def username_must_not_be_empty(cls, v):
        if len(v) < 1:
            raise ValueError('Username must not be empty')
        return v.title()

    @validator('password')
    def password_must_be_8_characters(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v.title()

    @validator('password')
    def password_must_contain_special_char(cls, v):
        valid_chars = "!@#$%^&*()<>,.;:'[]{}=-0987654321"
        for char in valid_chars:
            if char in v:
                return v.title()
        raise ValueError('Password must contain one of the following characters: ' + valid_chars)

    @validator('password2')
    def passwords_must_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords must match')
        return v.title()


class UserRegisterResponse(BaseModel):
    status: bool
    text: str
