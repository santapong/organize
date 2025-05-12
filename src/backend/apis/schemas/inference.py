from pydantic import BaseModel


# Using to fix Parameter from chat.
class InferenceParams(BaseModel):
    
    def __init__(self):
        pass
    