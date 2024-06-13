from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging

logger = logging.getLogger("fastapi-logger")


def add_exception_handlers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"Validation Error: {str(exc)}")
        return JSONResponse(
            status_code=400,
            content={"detail": exc.errors()},
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )
