from . import models

users = [
    models.User(
        name = "admin",
        password = "admin",
        role = 0
    )
]

ecgs = {}

def check_user(username: str, password: str) -> models.User | None:
    for user in users:
        if user.name == username and user.password == password:
            return user

    return None

