from pydantic import BaseModel, Field, EmailStr, validator
from enum import Enum

class GetBotResponseSchema(BaseModel):
    message: str = Field(...)


class Role(str, Enum):
    subscriber = "subscriber"
    admin = "admin"


class FeedbackBase(BaseModel):
    person_name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr = Field(...)
    message: str = Field(...)

    class Config:
        orm_mode = True


class FeedbackCreateSchema(FeedbackBase):
    pass


class FeedbackSchema(FeedbackBase):
    id: int = Field(...)

    @validator("id")
    def validate_id(cls, v):
        if v < 0:
            raise ValueError("id must be zero and greater than zero")
        return 

