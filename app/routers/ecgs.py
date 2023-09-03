from fastapi import APIRouter, Depends, HTTPException, Body, Request

from ..dependencies import get_token_header
from .. import models
from .. import persistence
from .. import process
from ..auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/ecgs",
    tags=["ecgs"],
    dependencies=[Depends(JWTBearer(required_role=models.USER_ROLE))],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def read_ecgs(request: Request):
    user_id = request.state.user
    if user_id not in persistence.ecgs:
        raise HTTPException(status_code=404, detail="Can't find any ecgs")

    return persistence.ecgs[user_id]

@router.post("", responses={403: {"description": "Operation forbidden"}})
async def create_ecg(request: Request, ecg: models.Ecg = Body(...)):
    user_id = request.state.user
    if user_id not in persistence.ecgs:
        persistence.ecgs[user_id] = {}

    # if ecg exists overwrite
    persistence.ecgs[user_id][ecg.id] = process.calculate_ecg(ecg)

    return {"message": "Ecg processed."}
