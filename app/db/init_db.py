from .session import engine, Base
from .base import *  # Import all models
import logging

logger = logging.getLogger("fastapi-logger")


def init_db():
    logger.info("Creating database tables")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")


if __name__ == "__main__":
    init_db()
