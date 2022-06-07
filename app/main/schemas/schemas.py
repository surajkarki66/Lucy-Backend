from pydantic import BaseModel, Field
from enum import Enum

class GetBotResponseSchema(BaseModel):
    message: str = Field(...)


class Role(str, Enum):
    subscriber = "subscriber"
    admin = "admin"
