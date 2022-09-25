from sqlalchemy.orm import Session
from fastapi import  Depends, HTTPException, status


from app.infrastructure.database.db import get_db
from app.helpers.jwt_bearer import JWTBearer
from app.models.models import User


class UserService:
    @staticmethod
    def get_current_user(db: Session = Depends(get_db), token_payload: Session = Depends(JWTBearer())):
        ''' Similarly you can implement get_current_active_user '''
        
        id = token_payload["user_id"]
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with id: {id} does not exist")

        return user

