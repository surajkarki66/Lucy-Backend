from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum

from ..infrastructure.database.db import Base
from ..schemas.schemas import Role


class Intent(Base):
    __tablename__ = "intents"
    intent = Column(String(100), primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, nullable=False)
    question = Column(String(255), nullable=False, unique=True)
    intent = Column(String(100), ForeignKey(
        "intents.intent", ondelete="CASCADE"), nullable=False)
    intent = relationship("Intent")

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))



class Response(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True, nullable=False)
    response = Column(String, nullable=False, unique=True)
    intent = Column(String(100), ForeignKey(
        "intents.intent", ondelete="CASCADE"), nullable=False)
    intent = relationship("Intent")

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default="subscriber")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, nullable=False)
    person_name = Column(String(255), nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)