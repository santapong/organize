from pydantic import BaseModel


# Using to fix Parameter from chat.
class InternalParams(BaseModel):
    
    def __init__(self):
        pass
    