from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV_STATE: str
    API_NAME: str
    API_DESCRIPTION: str
    API_VERSION: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    HOST: str
    PORT: int

    class Config:
        env_file = ".env"


settings = Settings()