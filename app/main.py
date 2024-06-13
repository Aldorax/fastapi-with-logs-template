from fastapi import FastAPI
from app.middleware.logging_middleware import LoggingMiddleware
from app.exceptions.handlers import add_exception_handlers
from app.api.v1.endpoints import items
from app.core.logging_config import setup_logging
from app.db.init_db import init_db
import logging

setup_logging()
logger = logging.getLogger("fastapi-logger")

logger.info("Initializing the database")
init_db()

app = FastAPI()

app.add_middleware(LoggingMiddleware)
add_exception_handlers(app)

app.include_router(items.router, prefix="/api/v1/items")

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting the server at 0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    logger.info("Server stopped")
