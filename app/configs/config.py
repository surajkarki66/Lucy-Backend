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
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    JWT_EXPIRE_SECONDS: int
    SECRET_KEY: str
    ALGORITHM: str
    HOST: str
    PORT: int
    DEVICE: str
    MODEL_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()