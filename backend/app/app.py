from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(title="4353 Project")
app.include_router(api_router, prefix="/api")
