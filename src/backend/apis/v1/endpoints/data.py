from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Data"] # Wait to using Settings
GROUP = "Data"
PREFIX = "/data"

router = APIRouter()

# TODO : Need more plan with it.
# Using to Chat with AI
@router.get("/data")
def data():
    pass