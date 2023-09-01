from . import models

users = []

def check_user(data: models.User):
    for user in users:
        if user.name == data.name and user.password == data.password:
            return True
    return False

