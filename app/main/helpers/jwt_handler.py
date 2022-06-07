import time
import jwt

from typing import Dict
from app.main.config import settings


def signJWT(user_id: int, expires_in_seconds: int) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "iat": time.time(),
        "exp": time.time() + expires_in_seconds
    }
    token = jwt.encode(payload, settings.SECRET_KEY,
                       algorithm=settings.ALGORITHM)

    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        raise Exception("JWTError: token is not decoded!")