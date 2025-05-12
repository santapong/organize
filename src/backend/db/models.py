from sqlalchemy import (
    Column,
    Interger,
    String,
    Float,
    ForeignKey,
    JSON,
    )
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Need to can change schema
class UserAuth(Base):
    __TABLENAME__ = "user"
    
class UserMap(Base):
    pass

class LLMModel(Base):
    pass

class History(Base):
    pass

class Internal(Base):
    pass

class Feedback(Base):
    pass