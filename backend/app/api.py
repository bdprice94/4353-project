import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from table_defs.user_register import UserRegister, UserRegisterResponse
from table_defs.user_login import UserLogin, UserLoginResponse


class BackendStub:
    # Will need to actually update DB, as well as deal with/return errors
    @staticmethod
    def add_user_profile(user_profile: UserRegister) -> UserRegisterResponse:
        return UserRegisterResponse(status=True, text="")

    @staticmethod
    def attempt_user_login(user_login: UserLogin) -> UserLoginResponse:
        if user_login.username != "Ben":
            return UserLoginResponse(status=False, text="User does not exist")
        return UserLoginResponse(status=True, text="")


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# ideally there would be a proper place to store build artifacts for deployment
# but for now this is just to mess around with since I'm bored
Path("../frontend/build").mkdir(parents=True, exist_ok=True)
build_dir = os.path.abspath('../frontend/build')
app.mount("/static_test", StaticFiles(directory=build_dir), name="static_test")


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list"}


@app.post("/create_user", tags=["create_user"])
async def post_user_profile(user_profile: UserRegister) -> UserRegisterResponse:
    return BackendStub.add_user_profile(user_profile)

@app.post("/login", tags=["login"])
async def post_user_login(user_login: UserLogin) -> UserLoginResponse:
    return BackendStub.attempt_user_login(user_login)
