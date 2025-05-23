from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Internal"] # Wait to using Settings
GROUP = "Private"
PREFIX = "Private"

app = APIRouter(prefix='/private')

# TODO : Need more plan with it.
# Using to Chat with AI
@app.get("/ai")
def inference():
    pass