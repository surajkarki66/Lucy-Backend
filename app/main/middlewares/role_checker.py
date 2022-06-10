from typing import List
from sqlalchemy.orm import Session
from fastapi import  Depends, HTTPException


from app.main.schemas.schemas import UserSchema
from app.main.services.user_service import UserService


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: UserSchema = Depends(UserService.get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")

        return user

