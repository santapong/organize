from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Dashboard"] # Wait to using Settings
GROUP = "Dashboard"
PREFIX = "/dashboard"

app = APIRouter(prefix=PREFIX)

# TODO : Need more plan with it.
# Using to Chat with AI
@app.get("/test")
def inference():
    pass