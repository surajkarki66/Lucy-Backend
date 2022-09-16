from typing import List
from fastapi import status, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter


from app.main.models.models import Query, Intent
from app.main.infrastructure.database.db import get_db
from app.main.schemas.schemas import QueryCreateSchema, QuerySchema, QueryUpdateSchema
from app.main.middlewares.role_checker import RoleChecker


router = APIRouter(prefix='/query')
allow_view_resource = RoleChecker(["admin"])
allow_update_resource = allow_view_resource
allow_create_resource = allow_update_resource


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=QuerySchema, dependencies=[Depends(allow_create_resource)])
def create_query(query: QueryCreateSchema, db: Session = Depends(get_db) ) -> dict : 
    intent_get = db.query(Intent).filter(Intent.title == query.intent)
    intent_get = intent_get.first()
    
    if intent_get is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"intent with title: {query.intent} does not exist")


    query_get = db.query(Query).filter(Query.text == query.text)
    query_get = query_get.first()
    if query_get:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"query with text: {query_get.text} already exist")

    new_query = Query(**query.dict())
    db.add(new_query)
    db.commit()
    db.refresh(new_query)

    return new_query


@router.get('/get', status_code=status.HTTP_200_OK, response_model=List[QuerySchema],
            dependencies=[Depends(allow_view_resource)])
def get_queries(db: Session = Depends(get_db), limit: int = 10,
              skip: int = 0) -> List[dict]:
    queries = db.query(Query).limit(limit).offset(skip).all()
    return queries


@router.get('/{id}', response_model=QuerySchema,
            dependencies=[Depends(allow_view_resource)])
def get_one_query(id: str, db: Session = Depends(get_db)) -> dict:
    query = db.query(Query).filter(Query.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Query with id: {id} does not exist")

    return query


@router.patch("/{id}", response_model=QuerySchema, dependencies=[Depends(allow_update_resource)])
def update_query(id: str, updated_query: QueryUpdateSchema,
                db: Session = Depends(get_db)):

    query_query = db.query(Query).filter(Query.id == id)
    query = query_query.first()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"query with id: {id} does not exist")
    
    intent_get = db.query(Intent).filter(Intent.title == updated_query.intent)
    intent_get = intent_get.first()
    if intent_get is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"intent with title: {query.intent} does not exist")
    
             
    query_query.update(updated_query.dict(), synchronize_session=False)

    db.commit()

    return query


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(allow_update_resource)])
def delete_query(id: str, db: Session = Depends(get_db)) -> dict:
    query_query = db.query(Query).filter(Query.id == id)
    query = query_query.first()

    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"query with id: {id} does not exist")

    query_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)