from pydantic import BaseModel


class UserRegister(BaseModel):
    username:  str
    password:  str
    password2: str

    def is_valid(self) -> bool:
        if len(self.username) < 1:
            return False
        if len(self.password) < 8:
            return False
        for char in self.password:
            if char in "!@#$%^&*()<>,.;:'[]{}=-0987654321":
                return True
        return False


class UserRegisterResponse(BaseModel):
    status: bool
    text: str
