class IncludeAPIRouter(object):
    def __new__(cls):
        from fastapi.routing import APIRouter
        from app.main.routers.hello_world import router as router_hello_world
     
        router = APIRouter()
        router.include_router(router_hello_world, prefix='/api/v1', tags=['hello_world'])

        return router


class DataBaseInstance(object):
    def __new__(cls):
        from app.main.infrastructure.database.db import get_db
        return get_db


# instance creation
get_db_instance = DataBaseInstance()
