from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth_handler import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True, required_role: int = -1):
        self.required_role = required_role
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials | None = await super(JWTBearer, self).__call__(request)

        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

        if not credentials.scheme == "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

        payload = decodeJWT(credentials.credentials)
        if not payload:
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")

        if not self.is_authorized(payload['user_role']):
            raise HTTPException(status_code=403, detail="Not Authorized.")

        request.state.user = payload['user_id']

        return credentials.credentials

    def is_authorized(self, required_role: int) -> bool:
        if self.required_role == -1:
            return True

        return self.required_role == required_role
