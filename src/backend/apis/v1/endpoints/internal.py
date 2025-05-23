from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Internal"] # Wait to using Settings
GROUP = "Private"
PREFIX = "/private"

router = APIRouter()

# TODO : Need more plan with it.
# Using to Chat with AI
@router.get("/internal")
def internal():
    pass