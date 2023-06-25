from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from table_defs.user_register import UserRegister, UserRegisterResponse
from table_defs.user_login import UserLogin, UserLoginResponse

import sqlalchemy
from sqlalchemy import text
from .database.db_manager import get_engine


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


db_engine = get_engine()
app = FastAPI()
origins = ["*"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list"}


@app.post("/create_user", tags=["create_user"])
async def post_user_profile(user_profile: UserRegister):
    return BackendStub.add_user_profile(user_profile)


@app.post("/login", tags=["login"])
async def post_user_login(user_login: UserLogin):
    return BackendStub.attempt_user_login(user_login)


@app.get("/database/tables")
async def get_database_tables():
    inspection = sqlalchemy.inspect(db_engine)
    db_names = inspection.get_table_names()

    return db_names


@app.post("/database/create_user_table")
async def create_user_table():
    with db_engine.connect() as connection:
        query = "CREATE TABLE users (id int, name varchar(255))"
        connection.execute(text(query))
        connection.commit()
        connection.close()

    return "Done"


@app.post("/database/create_user")
async def create_user(username: str):
    with db_engine.connect() as connection:
        query = text(f"INSERT INTO users (id, name) VALUES (0, '{username}')")
        result = connection.execute(query)
        print(result)
        connection.commit()
        connection.close()

    return "Done inserting"


@app.get("/database/get_users")
async def get_users():
    with db_engine.connect() as connection:
        query = text(f"SELECT * FROM users")
        result = connection.execute(query)
        users = result.fetchall()
        usernames = []
        for (id, user) in users:
            usernames.append(user)

        connection.commit()
        connection.close()

    return usernames
