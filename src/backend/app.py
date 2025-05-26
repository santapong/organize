import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backend.apis import v1
from src.backend.utils.settings import SettingsAPI

app = FastAPI()

# Class Settings API
# Origins: Str Read from .env

# Config CORS
origins = [
    SettingsAPI().origins # DEV Environment
]

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Add Origins
    allow_credentials=True, # Allow cookie
    allow_methods=["*"], # Allow method [GET, POST, DELETE, PUT, ...]
    allow_headers=["*"], # Allow header
)

# Adding Router /api/v1 
app.include_router(
    router=v1.router, 
    prefix=v1.PREFIX,
    tags=v1.TAGS
    )


if __name__ == "__main__":
    uvicorn.run('app:app', port=9002, reload=True)