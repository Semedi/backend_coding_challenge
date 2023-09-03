from . import models

users = [
    models.User(
        name = "admin",
        password = "admin",
        role = 0
    ),
    models.User(
        name = "test",
        password = "test",
        role = 1
    )
]

ecgs = {}

def check_user(username: str, password: str) -> models.User | None:
    for user in users:
        if user.name == username and user.password == password:
            return user

    return None
