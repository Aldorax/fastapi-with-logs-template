import logging
from logging.config import dictConfig
import os


class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.pathname.startswith(os.getcwd()):
            record.pathname = os.path.relpath(record.pathname, os.getcwd())
        return super().format(record)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": CustomFormatter,
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "logs/app.log",
            "formatter": "detailed",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    },
}


def setup_logging():
    dictConfig(LOGGING_CONFIG)


setup_logging()
