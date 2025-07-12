from litestar.dto import dto_field
from litestar.plugins.sqlalchemy import SQLAlchemyDTO

from pydantic import BaseModel
# Need more learning

class Agents(BaseModel):
    pass

class AgentID(BaseModel):
    pass

class Cards(BaseModel):
    pass

class CardID(BaseModel):
    pass

class AgentReadDTO()