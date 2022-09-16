class IncludeAPIRouter(object):
    def __new__(cls):
        from fastapi.routing import APIRouter
        from app.main.routers.hello_world import router as router_hello_world
        from app.main.routers.chat_bot import router as router_chat_bot
        from app.main.routers.feedback import router as router_feedback
        from app.main.routers.intent import router as router_intent
        from app.main.routers.query import router as router_query
        from app.main.routers.response import router as router_response
        from app.main.routers.auth import router as router_auth
        
        router = APIRouter()
        router.include_router(router_hello_world, prefix='/api/v2', tags=['hello_world'])
        router.include_router(router_chat_bot, prefix='/api/v2', tags=['chat_bot'])
        router.include_router(router_feedback, prefix='/api/v2', tags=['feedback'])
        router.include_router(router_auth, prefix="/api/v2", tags=["auth"])
        router.include_router(router_intent, prefix="/api/v2", tags=["intent"])
        router.include_router(router_query, prefix="/api/v2", tags=["query"])
        router.include_router(router_response, prefix="/api/v2", tags=["response"])

        return router


class DataBaseInstance(object):
    def __new__(cls):
        from app.main.infrastructure.database.db import get_db
        return get_db


# instance creation
get_db_instance = DataBaseInstance()
