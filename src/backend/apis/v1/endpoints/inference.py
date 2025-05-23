from fastapi import APIRouter, Depends


# FIX PARAMETER 
TAGS = ["Infer"] # Wait to using Settings
GROUP = "Infer"
PREFIX = "/infer"

router = APIRouter()

# TODO : Need more plan with it.
# Using to Chat with AI
@router.get("/inference")
def inference():
    pass