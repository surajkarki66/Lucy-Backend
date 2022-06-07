from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter


from app.main.models.models import Feedback
from app.main.infrastructure.database.db import get_db
from app.main.schemas.schemas import FeedbackCreateSchema, FeedbackSchema


router = APIRouter(prefix='/feedback')


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FeedbackSchema)
def create_feedback(feedback: FeedbackCreateSchema, db: Session = Depends(get_db) ) -> dict : 
    new_feedback = Feedback(**feedback.dict())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback

