from typing import List
from fastapi import status, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter


from app.main.models.models import Intent
from app.main.infrastructure.database.db import get_db
from app.main.schemas.schemas import IntentCreateSchema, IntentSchema, IntentUpdateSchema
from app.main.middlewares.role_checker import RoleChecker


router = APIRouter(prefix='/intent')
allow_view_resource = RoleChecker(["admin"])
allow_update_resource = allow_view_resource
allow_create_resource = allow_update_resource


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=IntentCreateSchema, dependencies=[Depends(allow_create_resource)])
def create_intent(intent: IntentCreateSchema, db: Session = Depends(get_db) ) -> dict : 
    intent_query = db.query(Intent).filter(Intent.title == intent.title)
    intent_get = intent_query.first()
    if intent_get:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"intent with title: {intent_get.title} already exist")

    new_intent = Intent(**intent.dict())
    db.add(new_intent)
    db.commit()
    db.refresh(new_intent)

    return new_intent

@router.get('/get', status_code=status.HTTP_200_OK, response_model=List[IntentSchema],
            dependencies=[Depends(allow_view_resource)])
def get_intents(db: Session = Depends(get_db), limit: int = 10,
              skip: int = 0) -> List[dict]:
    intents = db.query(Intent).limit(limit).offset(skip).all()
    return intents

@router.get('/{title}', response_model=IntentSchema,
            dependencies=[Depends(allow_view_resource)])
def get_one_intent(title: str, db: Session = Depends(get_db)) -> dict:
    intent = db.query(Intent).filter(Intent.title == title).first()
    if not intent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Intent with title: {title} does not exist")

    return intent

@router.patch("/{title}", response_model=IntentSchema, dependencies=[Depends(allow_update_resource)])
def update_intent(title: str, updated_intent: IntentUpdateSchema,
                db: Session = Depends(get_db)):

    intent_query = db.query(Intent).filter(Intent.title == title)

    intent = intent_query.first()
    if intent is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"intent with title: {title} does not exist")
    
    else:
        if intent.intent_no != updated_intent.intent_no or intent.title != updated_intent.title:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not allowed")
                                
    intent_query.update(updated_intent.dict(), synchronize_session=False)

    db.commit()

    return intent_query.first()


@router.delete("/{title}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(allow_update_resource)])
def delete_intent(title: str, db: Session = Depends(get_db)) -> dict:
    intent_query = db.query(Intent).filter(Intent.title == title)
    intent = intent_query.first()

    if intent is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"intent with title: {title} does not exist")

    intent_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)