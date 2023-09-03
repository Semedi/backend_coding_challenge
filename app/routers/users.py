from fastapi import APIRouter, Body, Depends, Request
from .. import models
from .. import persistence
from ..auth.auth_handler import signJWT
from ..auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/users/create", tags=["users"], dependencies=[Depends(JWTBearer(required_role=models.ADMIN_ROLE))])
async def create_user(request: Request, user: models.User = Body(...)):

    # replace with db call, making sure to hash the password first
    persistence.users.append(user) 

    return {
        "message": "user created"
    }

@router.post("/users/login", tags=["users"])
async def user_login(username: str = Body(), password: str = Body()):
    muser = persistence.check_user(username, password)
    if muser is not None:
        return signJWT(muser.name, muser.role)

    return {
        "error": "Wrong login details!"
    }

@router.get("/users/me", tags=["users"], dependencies=[Depends(JWTBearer())])
async def read_user_me(request: Request):
    return {"username": request.state.user}
