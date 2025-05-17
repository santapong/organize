from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Infer"] # Wait to using Settings
GROUP = "Infer"
PREFIX = "/Infer"

app = APIRouter(prefix=PREFIX)

# TODO : Need more plan with it.
# Using to Chat with AI
@app.get("/ai")
def inference():
    pass