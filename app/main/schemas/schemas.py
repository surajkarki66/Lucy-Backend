from pydantic import BaseModel, Field


class GetBotResponseSchema(BaseModel):
    message: str = Field(...)
