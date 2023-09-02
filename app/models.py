from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

class Lead(BaseModel):
    name: str
    samples: int = 0
    signal: list[int]

class Ecg(BaseModel):
    id: str
    date: str
    leads: list[Lead]



