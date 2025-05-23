from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Data"] # Wait to using Settings
GROUP = "Data"
PREFIX = "/data"

app = APIRouter(prefix=PREFIX)

# TODO : Need more plan with it.
# Using to Chat with AI
@app.get("/test")
def inference():
    pass