from pydantic import BaseModel

class AgentModel(BaseModel):
    name: str
    prompt: str