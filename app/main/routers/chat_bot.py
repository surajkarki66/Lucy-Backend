import random

from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter

from app.main.models.models import Intent, Response
from app.main.infrastructure.database.db import get_db
from app.main.services.intent_classification_service import IntentClassificationService
from app.main.schemas.schemas import GetBotResponseSchema

classification_service = IntentClassificationService()
router = APIRouter(prefix='/bot')


@router.get("/chat", status_code=status.HTTP_200_OK, response_model=GetBotResponseSchema)
def get_bot_response(message: str, db: Session = Depends(get_db)) -> dict : 
    inp_x=message.lower()
    pred, prob = classification_service.predict(inp_x)
    print(prob)
    if prob > 0.7:
        link = None
        intent = db.query(Intent).filter(Intent.intent_no == int(pred)).first()
        print(intent.title)
        responses = db.query(Response).filter(Response.tag == str(intent.title)).all()
        response = random.choice(responses)

        if response.link:
            link = response.link
        return {"message": response.text, "link": link if link is not None else "", "probability": prob }
   
    else:
        return {"message": "Sorry! i unable to understand what your saying", "link": "", "probability": prob }

        
    
