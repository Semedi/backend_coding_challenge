from fastapi import APIRouter, Depends, HTTPException, Body

from ..dependencies import get_token_header
from .. import models

router = APIRouter(
    prefix="/ecgs",
    tags=["ecgs"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("")
async def read_ecgs():
    if not fake_items_db:
        raise HTTPException(status_code=404, detail="Can't find any ecgs")
    return fake_items_db


@router.post("", responses={403: {"description": "Operation forbidden"}})
async def create_ecg(ecg: models.Ecg = Body(...)):
    print(ecg)


    return {"item_id": "test", "name": "The great Plumbus"}
