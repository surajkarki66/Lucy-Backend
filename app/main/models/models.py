from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from main.infrastructure.database.db import Base


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


