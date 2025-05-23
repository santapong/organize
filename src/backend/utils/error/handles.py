from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

class APIsErrorHandling:
    def __init__(self, app: FastAPI):
        self.app = app
        self.register_handlers()

    def register_handlers(self):
        @self.app.exception_handler(StarletteHTTPException)
        async def http_exception_handler(request: Request, exc: StarletteHTTPException):
            logging.error(f"HTTP error: {exc.detail}")
            return JSONResponse(
                status_code=exc.status_code,
                content={"error": "HTTPException", "detail": exc.detail},
            )

        @self.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc: RequestValidationError):
            logging.error(f"Validation error: {exc.errors()}")
            return JSONResponse(
                status_code=422,
                content={"error": "ValidationError", "detail": exc.errors()},
            )

        @self.app.exception_handler(Exception)
        async def generic_exception_handler(request: Request, exc: Exception):
            logging.exception("Unhandled exception occurred")
            return JSONResponse(
                status_code=500,
                content={"error": "InternalServerError", "detail": "An unexpected error occurred."},
            )
