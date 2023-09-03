from pydantic import BaseModel

ADMIN_ROLE = 0
USER_ROLE = 1

class User(BaseModel):
    name: str
    password: str
    role: int = 1

class Lead(BaseModel):
    name: str
    samples: int = 0
    signal: list[int]

class Ecg(BaseModel):
    id: str
    date: str
    leads: list[Lead]



