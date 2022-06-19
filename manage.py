import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.initializer import IncludeAPIRouter
from app.main.config import settings

def get_application():
    _app = FastAPI(title=settings.API_NAME,
                   description=settings.API_DESCRIPTION,
                   version=settings.API_VERSION)

    _app.include_router(IncludeAPIRouter())

    origins = ["http://localhost:3000"]

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return _app


app = get_application()



@app.on_event("shutdown")
def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    print("On App Shutdown this will be called.")

if __name__ == "__main__":
    uvicorn.run("manage:app", host=settings.HOST, port=settings.PORT, use_colors=True,reload=True)