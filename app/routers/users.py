from fastapi import APIRouter, Body
from .. import models
from .. import persistence
from ..auth.auth_handler import signJWT

router = APIRouter()


@router.post("/users/signup", tags=["users"])
async def create_user(user: models.User = Body(...)):
    # replace with db call, making sure to hash the password first
    persistence.users.append(user) 
    return {
        "message": "user created"
    }


@router.post("/user/login", tags=["users"])
async def user_login(user: models.User = Body(...)):
    if persistence.check_user(user):
        return signJWT(user.name)
    return {
        "error": "Wrong login details!"
    }

@router.get("/users/", tags=["users"])
async def read_users():
    return models.persistence


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
