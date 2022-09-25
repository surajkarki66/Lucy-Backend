from typing import List
from fastapi import status, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter


from app.models.models import Feedback
from app.infrastructure.database.db import get_db
from app.schemas.schemas import FeedbackCreateSchema, FeedbackSchema
from app.middlewares.role_checker import RoleChecker


router = APIRouter(prefix='/feedback')
allow_view_resource = RoleChecker(["admin"])
allow_update_resource = allow_view_resource


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=FeedbackSchema)
def create_feedback(feedback: FeedbackCreateSchema, db: Session = Depends(get_db) ) -> dict : 
    new_feedback = Feedback(**feedback.dict())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback


@router.get('/get', status_code=status.HTTP_200_OK, response_model=List[FeedbackSchema],
            dependencies=[Depends(allow_view_resource)])
def get_feedbacks(db: Session = Depends(get_db), limit: int = 10,
              skip: int = 0) -> List[dict]:
    feedbacks = db.query(Feedback).limit(limit).offset(skip).all()
    return feedbacks

@router.get('/{id}', response_model=FeedbackSchema,
            dependencies=[Depends(allow_view_resource)])
def get_one_feedback(id: str, db: Session = Depends(get_db)) -> dict:
    feedback = db.query(Feedback).filter(Feedback.id == id).first()
    if not feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Feedback with id: {id} does not exist")

    return feedback


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(allow_update_resource)])
def delete_feedback(id: str, db: Session = Depends(get_db)) -> dict:
    feedback_query = db.query(Feedback).filter(Feedback.id == id)
    feedback = feedback_query.first()

    if feedback is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feedback with id: {id} does not exist")

    feedback_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)