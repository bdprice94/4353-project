from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os


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
build_dir = os.path.abspath('../frontend/build')
app.mount("/static_test", StaticFiles(directory=build_dir), name="static_test")

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list"}
