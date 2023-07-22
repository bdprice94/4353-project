from fastapi import APIRouter
from app.api.endpoints import users
from app.api.endpoints import profile
from app.api.endpoints import fuelquote

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(fuelquote.router, prefix="/fuelquote", tags=["fuelquote"])
