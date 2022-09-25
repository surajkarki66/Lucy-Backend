class IncludeAPIRouter(object):
    def __new__(cls):
        from fastapi.routing import APIRouter
        from app.routers.chat_bot import router as router_chat_bot
        from app.routers.feedback import router as router_feedback
        from app.routers.intent import router as router_intent
        from app.routers.query import router as router_query
        from app.routers.response import router as router_response
        from app.routers.auth import router as router_auth
        
        router = APIRouter()
        router.include_router(router_chat_bot, prefix='/api/v2', tags=['chat_bot'])
        router.include_router(router_feedback, prefix='/api/v2', tags=['feedback'])
        router.include_router(router_auth, prefix="/api/v2", tags=["auth"])
        router.include_router(router_intent, prefix="/api/v2", tags=["intent"])
        router.include_router(router_query, prefix="/api/v2", tags=["query"])
        router.include_router(router_response, prefix="/api/v2", tags=["response"])

        return router


class DataBaseInstance(object):
    def __new__(cls):
        from app.infrastructure.database.db import get_db
        return get_db


# instance creation
get_db_instance = DataBaseInstance()
