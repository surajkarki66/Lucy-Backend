from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr, validator, SecretStr
from enum import Enum


# User
class Role(str, Enum):
    subscriber = "subscriber"
    admin = "admin"

class UserCreateSchema(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6)


class UserSchema(BaseModel):
    id: UUID = Field(...)
    first_name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    email: EmailStr = Field(...)
    password: SecretStr = Field(...)
    role: Role = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    class Config:
        orm_mode = True



class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6)


class TokenSchema(BaseModel):
    access_token: str = Field(...)



class UserUpdateSchema(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=32)
    last_name: str = Field(..., min_length=2, max_length=32)
    updated_at: datetime = Field(default_factory=datetime.now)


class PasswordUpdateSchema(BaseModel):
    old_password: str = Field(..., min_length=6)
    password: str = Field(..., min_length=6)
    updated_at: datetime = Field(default_factory=datetime.now)

# Feedback
class FeedbackBase(BaseModel):
    person_name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr = Field(...)
    message: str = Field(...)

    class Config:
        orm_mode = True

class FeedbackCreateSchema(FeedbackBase):
    pass

class FeedbackSchema(FeedbackBase):
    id: UUID = Field(...)

    
# Bot
class GetBotResponseSchema(BaseModel):
    message: str = Field(...)
    link: str = Field(...)

# Intent
class IntentBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    intent_no: int =Field(...)

    class Config:
        orm_mode = True

class IntentCreateSchema(IntentBase):
    pass

class IntentSchema(IntentBase):
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

class IntentUpdateSchema(IntentBase):
    updated_at: datetime = Field(default_factory=datetime.now)
    pass

# Queries
class QueryBase(BaseModel):
    text: str = Field(..., min_length=5, max_length=500)
    intent: str = Field(..., min_length=1, max_length=255)

    class Config:
        orm_mode = True

class QueryCreateSchema(QueryBase):
    pass

class QuerySchema(QueryBase):
    id: UUID = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)


class QueryUpdateSchema(QueryBase):
    updated_at: datetime = Field(default_factory=datetime.now)
    pass

# Response
class ResponseBase(BaseModel):
    text: str = Field(..., min_length=5, max_length=1000)
    link: Optional[str] = Field(None, min_length=1, max_length=255)
    tag: str = Field(..., min_length=2, max_length=255)

    class Config:
        orm_mode = True

class ResponseCreateSchema(ResponseBase):
    pass

class ResponseSchema(ResponseBase):
    id: UUID = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)


class ResponseUpdateSchema(ResponseBase):
    updated_at: datetime = Field(default_factory=datetime.now)
    pass
