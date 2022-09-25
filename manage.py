import uvicorn

from app.configs.config import settings

if __name__ == "__main__":
    uvicorn.run("app.app:app", host=settings.HOST, port=settings.PORT, use_colors=True,reload=True)