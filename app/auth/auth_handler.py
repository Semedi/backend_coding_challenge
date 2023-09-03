import time
from typing import Dict

import jwt


# should not be here
JWT_SECRET = "this_is_a_secret"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id: str, user_role: int) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "user_role": user_role,
        "expires": time.time() + 600,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] >= time.time(): 
            return decoded_token 

    except:
        pass

    return {}

