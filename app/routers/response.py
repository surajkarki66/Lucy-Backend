from typing import List
from fastapi import status, Depends, Response as R, HTTPException
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter


from app.models.models import Response, Intent
from app.infrastructure.database.db import get_db
from app.schemas.schemas import ResponseCreateSchema, ResponseSchema, ResponseUpdateSchema
from app.middlewares.role_checker import RoleChecker


router = APIRouter(prefix='/response')
allow_view_resource = RoleChecker(["admin"])
allow_update_resource = allow_view_resource
allow_create_resource = allow_update_resource


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=ResponseSchema, dependencies=[Depends(allow_create_resource)])
def create_response(response: ResponseCreateSchema, db: Session = Depends(get_db) ) -> dict : 
    intent_get = db.query(Intent).filter(Intent.title == response.tag)
    intent_get = intent_get.first()
    
    if intent_get is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"intent with title: {response.tag} does not exist")


    response_get = db.query(Response).filter(Response.text == response.text)
    response_get = response_get.first()
    if response_get:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"response with text: {response_get.text} already exist")

    new_response = Response(**response.dict())
    db.add(new_response)
    db.commit()
    db.refresh(new_response)

    return new_response


@router.get('/get', status_code=status.HTTP_200_OK, response_model=List[ResponseSchema],
            dependencies=[Depends(allow_view_resource)])
def get_responses(db: Session = Depends(get_db), limit: int = 10,
              skip: int = 0) -> List[dict]:
    responses = db.query(Response).limit(limit).offset(skip).all()
    return responses


@router.get('/{id}', response_model=ResponseSchema,
            dependencies=[Depends(allow_view_resource)])
def get_one_response(id: str, db: Session = Depends(get_db)) -> dict:
    response = db.query(Response).filter(Response.id == id).first()
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Query with id: {id} does not exist")

    return response


@router.patch("/{id}", response_model=ResponseSchema, dependencies=[Depends(allow_update_resource)])
def update_response(id: str, updated_response: ResponseUpdateSchema,
                db: Session = Depends(get_db)):

    response_query = db.query(Response).filter(Response.id == id)
    response = response_query.first()
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"response with id: {id} does not exist")
    
    intent_get = db.query(Intent).filter(Intent.title == updated_response.tag)
    intent_get = intent_get.first()
    if intent_get is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"intent with title: {response.tag} does not exist")
    
             
    response_query.update(updated_response.dict(), synchronize_session=False)

    db.commit()

    return response


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(allow_update_resource)])
def delete_response(id: str, db: Session = Depends(get_db)) -> dict:
    response_query = db.query(Response).filter(Response.id == id)
    response = response_query.first()

    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"response with id: {id} does not exist")

    response_query.delete(synchronize_session=False)
    db.commit()
    return R(status_code=status.HTTP_204_NO_CONTENT)