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
