from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlalchemy
from sqlalchemy import text
from ..database.db_manager import get_engine

db_engine = get_engine()

app = FastAPI()
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
