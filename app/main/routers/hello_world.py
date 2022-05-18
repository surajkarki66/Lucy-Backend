from fastapi.responses import JSONResponse
from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def hello_world():
    return JSONResponse(content={"message": "Hello World! 👍🏻"}, status_code=200)
