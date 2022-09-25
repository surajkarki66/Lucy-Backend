import uuid

from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Enum, ForeignKey

from ..infrastructure.database.db import Base
from ..schemas.schemas import Role


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=generate_uuid)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default="subscriber")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))


class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(String, primary_key=True, default=generate_uuid)
    person_name = Column(String(255), nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)

class Intent(Base):
    __tablename__ = "intents"
    title = Column(String(255), primary_key=True, nullable=False)
    intent_no = Column(Integer, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

class Query(Base):
    __tablename__ = 'queries'
    id = Column(String, primary_key=True, default=generate_uuid)
    text = Column(String(500), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

    intent = Column(String(255), ForeignKey(
        "intents.title", ondelete="CASCADE"), nullable=False)

    intent_details = relationship("Intent")


class Response(Base):
    __tablename__ = 'responses'
    id = Column(String, primary_key=True, default=generate_uuid)
    text = Column(String(1000), unique=True, nullable=False)
    link = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=expression.text('now()'))

    tag = Column(String(255), ForeignKey(
        "intents.title", ondelete="CASCADE"), nullable=False)

    tag_details = relationship("Intent")

    

