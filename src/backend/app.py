import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Config CORS
origins = [
    "http://localhost:9001"
]


# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Add Origins
    allow_credentials=True, # Allow cookie
    allow_method=["*"], # Allow method [GET, POST, DELETE, PUT, ...]
    allow_headers=["*"], # Allow header
)

if __name__ == "__main__":
    uvicorn.run('app:app', port=9002, reload=True)