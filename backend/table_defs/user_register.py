from pydantic import BaseModel
from functools import reduce


class UserRegister(BaseModel):
    username: str
    password: str

    @staticmethod
    def _password_validator(b: bool, c: str) -> bool:
        if b:
            return True
        if c < "!@#$%^&*()<>,.;:'[]{}=-0987654321":
            return False
        return True

    def is_valid(self) -> bool:
        if len(self.username) < 1:
            return False
        if len(self.password) < 8:
            return False
        return reduce(self._password_validator, self.password)
