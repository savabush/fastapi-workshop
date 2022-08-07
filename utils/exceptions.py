from fastapi import HTTPException, status
from typing import Any


class NotAuthorized(HTTPException):
    def __init__(self) -> None:
        status_code: int = status.HTTP_401_UNAUTHORIZED
        detail: Any = 'Could not validate credentials'
        headers = {
                'WWW-Authenticate': 'Bearer'
            }
        super().__init__(status_code=status_code, detail=detail, headers=headers)
