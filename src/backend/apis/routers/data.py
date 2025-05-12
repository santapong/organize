from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = [""] # Wait to using Settings
GROUP = ""
PREFIX = ""

app = APIRouter(prefix='/dashboard')

# TODO : Need more plan with it.
# Using to Chat with AI
@app.get("/test")
def inference():
    pass