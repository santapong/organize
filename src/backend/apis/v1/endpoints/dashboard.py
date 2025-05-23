from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Dashboard"] # Wait to using Settings
GROUP = "Dashboard"
PREFIX = "/dashboard"

router = APIRouter()

# TODO : Need more plan with it.
# Using to Chat with AI
@router.get("/dashboard")
def dashboard():
    pass